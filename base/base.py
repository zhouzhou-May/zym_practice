"""基于原生的selenium做二次封装"""
from selenium import webdriver
import time


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, locator):
        """定位元素，若定位到则返回，否则timeout异常"""
        if not isinstance(locator, tuple):
            print("")


