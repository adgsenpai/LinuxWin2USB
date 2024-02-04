#!/env/bin/python3
"""
Download url downloads the os
"""
from utils.download_progress import  DownloadProgressBar
import urllib.request

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