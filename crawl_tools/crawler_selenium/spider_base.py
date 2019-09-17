from abc import abstractmethod
from selenium import webdriver
import time


class SeleniumSpiderBase:
    def __init__(self):
        self.driver = webdriver.Chrome('Selenium\Drivers\chromedriver.exe')

    @abstractmethod
    def crawl_list(self):
        pass

    @abstractmethod
    def crawl_item(self, url):
        pass

    @abstractmethod
    def get_urls(self):
        pass

    def scroll_to_end(self, num):
        i = 0
        while i <= num:
            height = self.driver.get_window_size()
            self.driver.execute_script(f"window.scrollTo(0, {height['height'] * i+1});")
            time.sleep(2)
            i = i+1
