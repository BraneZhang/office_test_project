#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from businessView.weReadView import WeReadView
from common.myunit import StartEnd


class TestWeRead(StartEnd):

    def test_weRead(self):
        logging.info('======test_weRead=====')
        we = WeReadView(self.driver)
        we.select_index()
        book = 'Python学习手册（原书第4版）'
        page = 1000
        we.read(book,page)