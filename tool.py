#!/usr/bin/env python3

import os
import subprocess
# Linux Tool to create a bootable Windows 11 ISO on a USB drive
import sys

from utils import clean_workspace
from utils import create_bootable_usb_windows, check_if_os_exists
from utils import download_windows11
from utils import get_removable_drives_linux


def select_drive():
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
            return USBDrive
        else:
            print("Invalid selection. ")
            select_drive()


def select_os_path():
    # if windows11.iso is downloaded, ask user to proceed
    if os.path.isfile('windows11.iso'):
        print("Windows11 is already downloaded.\n"
              "\t1.Proceed with installation\n"
              "\t2.Select iso from another location\n"
              "\t3.Download windows11 iso again\n")
        selection = input("Enter your selection: ")
        if selection.isdigit():
            if selection == '3':
                download_windows11()
                return "windows11.iso"
            elif selection == '1':
                return "windows11.iso"
            elif selection == '2':
                os_selection = input("Enter your OS PATH {eg. /home/johnny/Downloads/Windows 11}: ")
                if not check_if_os_exists(os_selection):
                    print("OS path does not exist")
                    select_os_path()
                else:
                    return os_selection
            else:
                print("Invalid selection")
                select_os_path()
        else:
            print("Invalid input.")
    else:
        # select a windows iso from another location
        print("\t1.Select iso from location\n"
              "\t2.Download windows11 iso\n")
        selection = input()
        if selection == '2':
            # delete existing windows11.iso
            clean_workspace()
            download_windows11()
            return "windows11.iso"
        elif selection == '1':
            os_selection = input("Enter your OS PATH {eg. /home/johnny/Downloads/Windows 11}: ")
            if not check_if_os_exists(os_selection):
                print("OS path does not exist")
                select_os_path()
            else:
                return os_selection


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
    USBDrive = select_drive()
    os_path = select_os_path()

    print("OS PATH",os_path)

    if check_if_os_exists(os_path):
        create_bootable_usb_windows(USBDrive, os_path)
        print('Windows 11 bootable USB successfully created on ' + USBDrive)
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
