#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2023 Chatopera Inc. <chatopera.com> All Rights Reserved
#
# Author: Hai Liang Wang
# Date: 2023-11-14:18:04:24
#
#===============================================================================

"""

"""
__copyright__ = "Copyright (c) 2023 Chatopera Inc. All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2023-11-14:18:04:24"

import os
import shutil
import sys
import tempfile

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

import json
import ssl
import requests
import urllib.request as request
import urllib.parse as urlparse
import email.header
from chatoperastore.logger import Logger, LN
from chatoperastore.exceptions import LicensedfileDownloadException
from chatoperastore.console_output import callback_progress, bar_adaptive

logger = Logger(LN(__file__))
requests.packages.urllib3.disable_warnings()

def decode_mime_words(s):
    """
    This is a MIME encoded-word, parse it with email.header
    https://stackoverflow.com/questions/12903893/python-imap-utf-8q-in-subject-string
    """
    return u''.join(
        word.decode(encoding or 'utf8') if isinstance(word, bytes) else word
        for word, encoding in email.header.decode_header(s))


def filename_from_url(url):
    """:return: detected filename or None"""
    fname = os.path.basename(urlparse.urlparse(url).path)
    if len(fname.strip(" \n\t.")) == 0:
        return None
    return fname


def filename_from_headers(headers):
    """Detect filename from Content-Disposition headers if present.
    http://greenbytes.de/tech/tc2231/

    :param: headers as dict, list or string
    :return: filename from content-disposition header or None
    """
    if type(headers) == str:
        headers = headers.splitlines()
    if type(headers) == list:
        headers = dict([x.split(':', 1) for x in headers])
    cdisp = headers.get("Content-Disposition")
    if not cdisp:
        return None
    cdtype_original = cdisp.split(';')
    cdtype = []
    for x in cdtype_original:
        x = x.strip()
        if x: cdtype.append(x)

    if len(cdtype) <= 1:
        return None
    if cdtype[0].strip().lower() not in ('inline', 'attachment'):
        return None
    # several filename params is illegal, but just in case
    fnames = [decode_mime_words(x) for x in cdtype[1:] if x.strip().startswith('filename=')]
    if len(fnames) < 1:
        return None
    name = fnames[0].split('=')[1].strip(' \t"')
    name = os.path.basename(name)
    if not name:
        return None
    return name


def filename_fix_existing(filename):
    """Expands name portion of filename with numeric '__x__' suffix to
    return filename that doesn't exist already.
    """
    dirname = '.'
    name, ext = filename.rsplit('.', 1)
    names = [x for x in os.listdir(dirname) if x.startswith(name)]
    names = [x.rsplit('.', 1)[0] for x in names]
    suffixes = [x.replace(name, '') for x in names]
    # filter suffixes that match ' (x)' pattern
    suffixes = [x[2:-1] for x in suffixes
                if x.startswith('__') and x.endswith('__')]
    indexes = [int(x) for x in suffixes
               if set(x) <= set('0123456789')]
    idx = 1
    if indexes:
        idx += sorted(indexes)[-1]
    return '%s__%d__.%s' % (name, idx, ext)


def __retrieve_metadata(url, data=None):
    """
    Get URL without check ssl
    https://stackoverflow.com/questions/36600583/python-3-urllib-ignore-ssl-certificate-verification
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    with request.urlopen(url, data, context=ctx) as f:
        data = f.read()
        return json.loads(data)


def get_metadata_filename(store_provider, license_id):
    """
    Get filename with meta json
    """
    meta_url = "%s/dl/%s.json" % (store_provider, license_id)
    meta_data = __retrieve_metadata(meta_url)

    if "rc" in meta_data and meta_data["rc"] == 0:
        if "data" in meta_data and \
            "productModel" in meta_data["data"] and "licensedfile" in meta_data["data"]["productModel"]:
            return meta_data["data"]["productModel"]["licensedfile"], meta_data["data"]["productModel"]["filesize"] if "filesize" in meta_data["data"]["productModel"] else 0
        else:
            LicensedfileDownloadException("UNEXPECTED DATA", "licensedfile not found.")

    raise LicensedfileDownloadException(meta_data["rc"] if "rc" in meta_data else "UNKNOWN", \
                                        meta_data["error"] if "error" in meta_data else "Get error during download metadata ...")


def __download_gz(url, fp, filesize):
    """
    Download gz file to filepath without SSL Checks
    """
    with requests.get(url, verify=False, stream=True) as fin, open(fp, 'b+w') as fout:
        fin.raise_for_status()
        print("[chatopera] store licensed file downloading is started, it takes minutes depending on your network ...\n")
        # fout.write(fin.read())
        block_trans = 0
        for chunk in fin.iter_content(chunk_size=8192):
            if chunk:  # filter out keep-alive new chunks
                fout.write(chunk)
                block_trans = block_trans + 1
                callback_progress(block_trans, len(chunk), filesize, bar_function=bar_adaptive)
    # mimic 100 pers downloads at last
    callback_progress(1, filesize, filesize, bar_function=bar_adaptive)
    print("\n[chatopera] store file download done.\n")


def download(store_provider, license_id, out=None, serverinst_id=None, service_name=None):
    """High level function, which downloads URL into tmp file in current
    directory and then renames it to filename autodetected from either URL
    or HTTP headers.

    :param bar: function to track download progress (visualize etc.)
    :param out: output filename or directory
    :return:    filename where URL is downloaded to
    """

    dl_url = "%s/dl/%s.gz" % (store_provider, license_id)

    if serverinst_id or service_name:
        dl_url += "?"

    if serverinst_id:
        dl_url += "serverId=%s" % serverinst_id

    if service_name:
        if not dl_url.endswith("?"):
            dl_url += "&"
        dl_url += "servicename=%s" % service_name

    logger.info("dl_url %s" % dl_url)

    names = dict()
    names["out"] = out or ''
    names["url"] = filename_from_url(dl_url)

    # verify license and get filename
    names["header"], filesize = get_metadata_filename(store_provider, license_id)

    # get filename for temp file in current directory
    prefix = (names["url"] or names["out"] or ".") + "."
    (fd, tmpfile) = tempfile.mkstemp(".tmp", prefix=prefix, dir=".")
    os.close(fd)
    os.unlink(tmpfile)

    __download_gz(dl_url, tmpfile, filesize)

    if os.path.isdir(names["out"]):
        filename = names["header"] or names["url"]
        filename = names["out"] + "/" + filename
    else:
        filename = names["out"] or names["header"] or names["url"]
    # add numeric ' (x)' suffix if filename already exists
    if os.path.exists(filename):
        filename = filename_fix_existing(filename)
    shutil.move(tmpfile, filename)

    return filename

##########################################################################
# Testcases
##########################################################################
import unittest

# run testcase: python /c/Users/Administrator/chatopera/store/sdk/python/tmp/foo.py Test.testExample
class Test(unittest.TestCase):
    '''

    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001(self):
        print("test_001")
        # data = get_url("http://localhost:7035/dl/LP400T38.json")
        # data = get_url("http://localhost:7035/dl/LP400T38.gz")
        fname = download("http://localhost:7035", "LP400T38")
        print("got,", fname)

def test():
    suite = unittest.TestSuite()
    suite.addTest(Test("test_001"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    test()

if __name__ == '__main__':
    main()
