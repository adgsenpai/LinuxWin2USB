#!/usr/bin/env python3
"""
Download url downloads the os
"""
from utils import DownloadProgressBar
import urllib.request


# def download_url(url, output_path):
#     with DownloadProgressBar(unit='B', unit_scale=True,
#                              miniters=1, desc='windows11.iso') as t:
#         opener = urllib.request.build_opener()
#         opener.addheaders = [
#             ('User-agent',
#              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
#              'Chrome/53.0.2785.143 Safari/537.36')]
#         urllib.request.install_opener(opener)
#         urllib.request.urlretrieve(
#             url, filename=output_path, reporthook=t.update_to)
def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc='windows11.iso') as t:
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-agent',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(
            url, filename=output_path, reporthook=t.update_to)


def download_windows11():
    try:
        download_url('https://www.itechtics.com/?dl_id=145', 'windows11.iso')
        print('Windows 11 ISO downloaded successfully.')
    except Exception as e:
        print('Error downloading Windows11.iso \n' + str(e))
