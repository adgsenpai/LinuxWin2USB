#!/usr/bin/env python3
from utils.clean_workspace import clean_workspace
from utils.create_bootable import create_bootable_usb_windows, check_if_os_exists
from utils.download_os import download_url, download_windows11
from utils.download_progress import DownloadProgressBar
from utils.get_removable_devices import get_removable_drives_linux
