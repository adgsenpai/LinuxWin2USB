# LinuxWin2USB

Creates a bootable Windows 11 USB drive from a Linux system. It also downloads the `Windows11.iso` file.

![usbboot](https://user-images.githubusercontent.com/45560312/185401576-c687b927-1224-4a68-a768-360567f7f38f.png)

![Screenshot 2022-08-18 150658](https://user-images.githubusercontent.com/45560312/185402335-19263df4-d527-42b2-8530-440c4cbc5601.png)

## Requirements
- PIP3
- Python3

## Installation

1. Clone repository

`git clone https://github.com/adgsenpai/LinuxWin2USB`

2. Install requirements

`sudo pip3 install -r requirements.txt`


## Usage

1. Run script

`sudo python3 tool.py`

or 

`sudo ./tool`



2. Follow all the prompts. You will be asked to select a USB drive. Your data will be destroyed on the device you choose and will be formatted as NTFS.

3. Reboot to your USB drive for usage of the Windows11ISO

