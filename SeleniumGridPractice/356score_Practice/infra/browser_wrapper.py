from selenium import webdriver

class BrowserWrapper:

    def __init__(self):
        self.driver = None
        print('test has started')

    def get_driver(self):
        self.driver = webdriver.Chrome
        return self.driver