from selenium import webdriver

class BrowserWrapper:

    PATH = "C:\Program Files (x86)\chromedriver.exe"

    def __init__(self):
        self.driver = None
        print('test has started')

    def get_driver(self, url=None):
        self.driver = webdriver.Chrome()
        if url:
            self.driver.get(url)
        return self.driver
