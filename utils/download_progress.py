#!/usr/bin/env python3
"""
The script contains the `DownloadProgressBar`
that shows the download progress of the windows 11
"""
import tqdm


class DownloadProgressBar(tqdm.tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total = None

    def update_to(self, byte=1, byte_size=1, total_size=None):
        if total_size is not None:
            self.total = total_size
        self.update(byte * byte_size - self.n)
