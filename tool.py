#!/usr/bin/env python3

import os
import subprocess
# Linux Tool to create a bootable Windows 11 ISO on a USB drive
import sys

from utils import clean_workspace
from utils import create_bootable_usb_windows
from utils import download_windows11
from utils import get_removable_drives_linux


def make_bootable():
    subprocess.call(['clear'])
    print('Welcome to the Windows 11 ISO USB Tool.')
    print('This tool will create a bootable Windows 11 ISO on a USB drive.')

    print('Information on storage devices:')
    print('---------------------------------')
    subprocess.call(['sudo', 'fdisk', '-l'])
    print('---------------------------------')
    print('Select USB drive to create a bootable USB of Windows 11 on:')
    print('-----------------------------------------')
    removable_drives = get_removable_drives_linux()
    usb_drives = list(removable_drives.values())
    for i, (label, path) in enumerate(removable_drives.items()):
        print("{}: {} - {}".format(i, label, path))
    print('-----------------------------------------')
    print('Enter the number of the drive you want to create a bootable USB of Windows 11 on:')
    selection = input()
    if selection.isdigit():
        selection = int(selection)
        if selection < len(usb_drives):
            print(usb_drives)
            USBDrive = usb_drives[selection]
            print('Selected USB drive: ' + USBDrive)
            # if windows11.iso is not downloaded, download it
            if not os.path.isfile('windows11.iso'):
                download_windows11()
            else:
                # ask if user wants to download windows11.iso again else continue
                print('Windows 11 ISO already downloaded. Do you want to download it again? (y/n)')
                selection = input()
                if selection == 'y':
                    # delete existing windows11.iso
                    clean_workspace()
                    download_windows11()
            create_bootable_usb_windows(USBDrive)
            print('Windows 11 bootable USB successfully created on ' + USBDrive)
        else:
            print('Invalid selection')
    else:
        print('Invalid selection')
    input('Press enter to exit')
    sys.exit()


if __name__ == '__main__':
    # make sure we run this in linux
    if os.name != 'posix':
        print('This script must be run in linux.')
        sys.exit(1)

    # make sure ran as root
    if os.geteuid() != 0:
        print('This script must be run as root')
        sys.exit(1)

    make_bootable()
