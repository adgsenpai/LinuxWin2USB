#!/usr/bin/env python3
import subprocess
import os


def check_if_drive_exists(drive_path):
    if os.path.exists(drive_path):
        print("Drive path verified")
    else:
        print("Drive does not exists.\
              Please check and try again")
        return


def create_bootable_usb_windows(USBDrive):
    # check if drive exists
    check_if_drive_exists(USBDrive)

    # Create a new USB drive
    subprocess.call(['clear'])
    print('Formatting USB drive...')
    # formatting the usb drive
    result = subprocess.call(['sudo', 'mkfs.ntfs', '-f', USBDrive, '-F'])
    if result != 0:
        print("Error during Formatting")
        return
    # clear output of console
    subprocess.call(['clear'])
    print("Moving Windows 11 ISO to USB drive...")
    subprocess.call(
        ['sudo', 'dd', 'bs=4M', 'if=windows11.iso', 'of={0}'.format(USBDrive), 'status=progress', 'oflag=sync'])
    print('ISO copied successfully.')
    # Unmount the USB drive
    print('Unmounting USB drive...')
    subprocess.call(['sudo', 'umount', USBDrive])
    print('USB drive unmounted successfully.')
