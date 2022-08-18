# Linux Tool to create a bootable Windows 11 ISO on a USB drive

import sys
import os
import urllib.request
from tqdm import tqdm
import subprocess

def get_removable_drives_linux():
    drives = []
    for drive in os.listdir('/sys/block'):
        if drive.startswith('sd'):
            drives.append(drive)
    return drives
    

def create_bootable_usb_windows(USBDrive):
    # Create a new USB drive
    print('Creating USB drive...')
    subprocess.call(['mkfs.ntfs', '-F', '-I', '-L', 'Windows11', USBDrive])
    print('USB drive created successfully.')
    # Mount the USB drive
    print('Mounting USB drive...')
    subprocess.call(['mount', USBDrive, '-t', 'ntfs', '-o', 'rw'])
    print('USB drive mounted successfully.')
    # Copy the ISO to the USB drive
    print('Copying ISO to USB drive...')
    subprocess.call(['cp', 'windows11.iso', USBDrive])
    print('ISO copied successfully.')
    # Unmount the USB drive
    print('Unmounting USB drive...')
    subprocess.call(['umount', USBDrive])
    print('USB drive unmounted successfully.')


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc='windows11.iso') as t:
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(
            url, filename=output_path, reporthook=t.update_to)


def CleanWorkspace():
    if os.path.isfile('windows11.iso'):
        os.remove('windows11.iso')
        return True
    else:
        return False


def DownloadWindows11():
    try:
        download_url('https://www.itechtics.com/?dl_id=145', 'windows11.iso')
        print('Windows 11 ISO downloaded successfully.')
    except Exception as e:
        print('Error downloading Windows11.iso \n' + str(e))


if __name__ == '__main__':
    print('Select USB drive to install Windows 11 on:')
    print('-----------------------------------------')
    removable_drives = get_removable_drives_linux()
    for i, drive in enumerate(removable_drives):
        print(str(i) + ': ' + drive)
    print('-----------------------------------------')
    print('Enter the number of the drive you want to install Windows 11 on:')
    selection = input()
    if selection.isdigit():
        selection = int(selection)
        if selection < len(removable_drives):
            USBDrive = removable_drives[selection]
            print('Selected USB drive: ' + USBDrive)
            if CleanWorkspace():
                DownloadWindows11()
                create_bootable_usb_windows(USBDrive)
                print('Windows 11 installed successfully on ' + USBDrive)
            else:
                print('Windows 11 is already installed on ' + USBDrive)
        else:
            print('Invalid selection')
    else:
        print('Invalid selection')
    input('Press enter to exit')
    sys.exit()