#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Device():
    dev = None
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





