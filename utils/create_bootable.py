#!/usr/bin/env python3
import subprocess
import os


def check_if_drive_exists(drive_path):
    if os.path.exists(drive_path):
        print("Drive path verified")
        return True
    else:
        print("Drive does not exists.\
              Please check and try again")
        return False


def create_bootable_usb_windows(USBDrive):
    # check if drive exists
    if not check_if_drive_exists(USBDrive):
        exit(1)
    # Create a new USB drive
    subprocess.call(['clear'])
    print('Formatting USB drive...')
    # formatting the usb drive
    result = subprocess.call(['sudo', 'mkfs.ntfs', '-f', USBDrive, '-F'])
    if result != 0:
        print("Error during Formatting. Are you sure you are root?")
        exit(1)
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
