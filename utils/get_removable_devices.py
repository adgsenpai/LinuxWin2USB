#!/usr/bin/env python3

# This is the function declaration for `get_removable_drives_linux`.
# This function is used to get all removable drives on a Linux machine.
# The function uses the `subprocess` module to execute the `lsblk` command, which lists block devices.
# From this list, it identifies storage devices ('sd' mentioned in the code is short for SCSI disk) using the `sd` keyword.
# `lsblk -o NAME,MOUNTPOINT` lists the name and mount points of block devices.
# It decodes the output of the command from bytes to a UTF-8 string, and then splits the string into lines.
# The function then checks each line for 'sd', if found it appends '/dev/' to the device name (line.split()[0]) and adds it to a list.
# The '/dev/' prefix is used to represent device files in Unix-like systems.
# Finally, the function returns the list containing the paths of all removable drives.
import subprocess


def get_removable_drives_linux():
    # get sd paths
    usb_devices = {}
    for line in subprocess.check_output(['lsblk', '-o', 'PATH,NAME,LABEL,MOUNTPOINT,SIZE']).decode('utf-8').split('\n'):
        if 'sd' in line:
            device_name = line.split()[1]
            device_label = line.split()[2]
            device_path = line.split()[0]
            removable_path = f"/sys/block/{device_name}/removable"

            try:
                with open(removable_path) as removable_file:
                    is_removable = int(removable_file.read().strip())
                    if is_removable:
                        usb_devices[device_label] = device_path
            except FileNotFoundError:
                pass  # Ignore non-existent removable file (not all devices have it)

    return usb_devices


removable_drives = get_removable_drives_linux()
print(removable_drives)