#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class Device():
    dev = '9613fafd'
    udid = None
    data = {}

    def set_dev(self, device):
        Device.dev = device

    def get_dev(self):
        return Device.dev

    def set_udid(self, udid):
        Device.udid = udid

    def get_udid(self):
        return Device.udid



if __name__ == '__main__':
    msg = os.system('adb shell ls /storage/emulated/0/yozoCloud/asdf.doc')
    print(f'msg:{msg}')

