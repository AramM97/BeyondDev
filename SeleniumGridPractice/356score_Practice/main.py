import time
import unittest
from selenium import webdriver
import concurrent.futures

from logic.mainPage import MainPage


class test(unittest.TestCase):
    HUB_URL = "http://192.168.1.32:4444/wd/hub"

    def setUp(self):
        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] = 'Windows 11'

        self.fireFox_cap = webdriver.FirefoxOptions()
        self.fireFox_cap.capabilities['platformName'] = 'Windows 11'

        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'Windows 11'

        #self.cap_list = [self.chrome_cap, self.fireFox_cap, self.edge_cap]
        self.cap_list = [self.chrome_cap]

    def test_run_grid_serial(self):
        for caps in self.cap_list:
            self.test5_execute(caps)

    def test_runs_serial(self):
            for caps in self.cap_list:
                self.test_execute(caps)
            for caps in self.cap_list:
                self.test2_execute(caps)
            for caps in self.cap_list:
                self.test3_execute(caps)
            for caps in self.cap_list:
                self.test4_execute(caps)
            for caps in self.cap_list:
                self.test5_execute(caps)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_execute, self.cap_list)

    def test_execute(self, caps):
        driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
        driver.get("https://www.365scores.com/he")


        time.sleep(3)
        self.main_page = MainPage(driver)
        self.main_page.switch_to_tennis_scores()

        title = driver.title
        print('title: ', title)
        expected_title = "365Scores"
        print("test run on: ", caps.capabilities)
        self.assertIn(expected_title, title, "Title doesn't match expected value")
        time.sleep(3)
        driver.quit()

    def test2_execute(self, caps):
        driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
        driver.get("https://www.365scores.com/he")

        time.sleep(3)
        self.main_page = MainPage(driver)

        timer_one = self.main_page.get_match_timer()
        time.sleep(1)
        timer_two = self.main_page.get_match_timer()

        print("test run on: ", caps.capabilities)
        self.assertNotEqual(timer_one, timer_two, "Timer CountDwown Doesn't Mover")
        time.sleep(3)
        driver.quit()

    def test3_execute(self, caps):
        driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
        driver.get("https://www.365scores.com/he")

        time.sleep(3)
        self.main_page = MainPage(driver)
        self.main_page.switch_to_live_view()

        title = driver.title
        print('title: ', title)
        expected_title = "לייב"
        print("test run on: ", caps.capabilities)
        self.assertIn(expected_title, title, "Title doesn't match expected value")
        time.sleep(3)
        driver.quit()

    def test4_execute(self, caps):
        driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
        driver.get("https://www.365scores.com/he")

        print(caps.capabilities["browserName"])

        time.sleep(3)
        self.main_page = MainPage(driver)
        self.main_page.search_flow("bayern munich")

        title = driver.title
        print('title: ', title)
        expected_title = "לייב"
        print("test run on: ", caps.capabilities)
        self.assertIn(expected_title, title, "Title doesn't match expected value")
        time.sleep(3)
        driver.quit()

    def test5_execute(self, caps):
        driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
        driver.get("https://www.365scores.com/he")

        print(caps.capabilities["browserName"])

        time.sleep(3)
        self.main_page = MainPage(driver)
        self.main_page.go_to_featured_game_page()

        title = driver.title
        print('title: ', title)
        expected_title = "לייב"
        print("test run on: ", caps.capabilities)
        self.assertIn(expected_title, title, "Title doesn't match expected value")
        time.sleep(3)
        driver.quit()
