#!/usr/bin/env python3


import os
def clean_workspace():
    if os.path.isfile('windows11.iso'):
        os.remove('windows11.iso')
