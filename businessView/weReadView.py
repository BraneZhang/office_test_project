#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from common.common_fun import Common


class WeReadView(Common):

    def search_book(self,book):
        self.driver.find_element(By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout'
                                           '/android.widget.LinearLayout').click()


    def select_index(self,index='书架'):
        index_dict={'发现':'rt','书架':'rw','想法':'ry','我':'s2'}
        self.driver.find_element(By.ID,'com.tencent.weread:id/%s'%index_dict[index]).click()

    def read(self, book,page=0):
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % book).click()
        for i in range(page-1):
            # self.swipeLeft()
            self.tap(930,1820)
