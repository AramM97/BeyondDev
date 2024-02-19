import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest

from selenium.webdriver.support.wait import WebDriverWait

from logic.youtube_page import YouTubePage
from logic.youtube_search_result_page import YouTubeSearchResultPage
from logic.youtube_video_page import YoutubeVideoPage

from infra.brower_wrapper import BrowserWrapper
from selenium.webdriver.support import expected_conditions as EC

import time


class YouTubePageTest(unittest.TestCase):
    def navigate_to_youtube_page(self ,link = "http://www.youtube.com"):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(link)
        self.youtube_page = YouTubePage(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))  # Replace with the actual identifier
        )

        return self.browser, self.driver, self.youtube_page

    def navigate_to_youtube_page(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        self.driver.implicitly_wait(3)

        return self.browser, self.driver, self.youtube_page


    def test_check_title_for_search(self):
        self.browser, self.driver, self.youtube_page = self.navigate_to_youtube_page()
        self.youtube_page.search_flow("Python Programming")
        time.sleep(3)
        self.title_page = self.driver.title
        print(self.title_page)

        self.assertIn("Python Programming", self.title_page, "The title does not show")
        # test/logic

    def test_check_filter_search(self):
        self.browser, self.driver, self.youtube_page = self.navigate_to_youtube_page()
        self.youtube_page.search_flow("Python Programming")
        time.sleep(3)
        self.youtube_page.press_on_filter()
        self.title_page = self.driver.title

        print(self.title_page)

        self.assertIn("Python Programming", self.title_page, "The title does not show")

    def test_podcasts_from_menu(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        time.sleep(3)

        self.youtube_page.open_menu()
        self.youtube_page.go_to_podcasts()
        time.sleep(3)
        self.youtube_page.go_to_podcasts_popular_episodes


    def test_music_from_menu(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        time.sleep(3)

        self.youtube_page.open_menu()
        self.youtube_page.go_to_youtube_music()
        time.sleep(3)
        self.youtube_page.go_to_playlist()


    def test_scroll_shorts(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        time.sleep(3)
        self.youtube_page.go_to_shorts()
        time.sleep(5)
        self.youtube_page.scroll_shorts()
        time.sleep(5)

    def test_shorts_comments(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        time.sleep(3)
        self.youtube_page.go_to_shorts()
        time.sleep(5)
        self.youtube_page.shorts_comments()
        time.sleep(5)

    def test_mute_shorts(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        time.sleep(3)
        self.youtube_page.go_to_shorts()
        time.sleep(5)
        self.youtube_page.mute_short()
        time.sleep(5)
'''
    def test_open_youtube_video(self):
        self.browser, self.driver, self.youtube_page = self.navigate_to_youtube_page()
        self.youtube_page.search_flow("Python Programming")
        self.title_page = self.driver.title
        print(self.title_page)
        self.youtube_result_page = YouTubeSearchResultPage(self.driver)
        self.youtube_result_page.click_first_video()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Python Programming"))

    def test_get_pinned_comment(self):
        # Replace with the URL of the video you want to test
        video_url = "https://www.youtube.com/watch?v=j7VZsCCnptM"

        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(video_url)
        self.youtube_video_page = YoutubeVideoPage(self.driver)

        # Get the pinned comment
        pinned_comment = self.youtube_video_page.get_pinned_comment()

        # Print or use the pinned comment as needed
        print("Pinned Comment:", pinned_comment)

    def test_make_full_screen(self):
        # Replace with the URL of the video you want to test
        video_url = "https://www.youtube.com/watch?v=g4N-X2YtNW4"

        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(video_url)
        self.youtube_video_page = YoutubeVideoPage(self.driver)

        self.youtube_video_page.make_video_full_screen()

'''


