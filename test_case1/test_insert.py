#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from businessView.insertView import InsertView
from common.myunit import StartEnd


class TestInsert(StartEnd):

    @unittest.skip("skip inssert SS")
    def test_insert_SS(self):
        types = 'ss'
        i = InsertView(self.driver)
        i.create_file(types)
        i.insert_SS()
        i.insert_common(types)
        i.save_close(types)

    # @unittest.skip("skip inssert PG")
    def test_insert_PG(self):
        types = 'pg'
        i = InsertView(self.driver)
        i.create_file(types)
        i.insert_PG()
        i.insert_common(types)
        i.save_close(types)

    @unittest.skip("skip inssert wp")
    def test_insert_WP(self):
        types = 'wp'
        i = InsertView(self.driver)
        i.create_file(types)
        i.insert_common(types)
        i.insert_PG()
        i.save_close(types)
