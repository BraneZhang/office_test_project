from selenium.webdriver.support.wait import WebDriverWait


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(3)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def click_element(self,*loc):
        self.driver.find_element(*loc).click()

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
