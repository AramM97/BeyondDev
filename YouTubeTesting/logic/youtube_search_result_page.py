from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage
import time

class YouTubeSearchResultPage(BasePage):
    VIDEO_TITLE_ID = "video-title"
    SEARCH_QUERY = "//input[@id='search']"

    def __init__(self, driver):
        super().__init__(driver)
        print('YouTubeSearchResultPage constructor')
        self.video_title_element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, self.VIDEO_TITLE_ID)))

        self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_QUERY)
        self.search_query = self.search_input.text

        print()


    def get_video_titles(self, n=5):
        video_urls = []
        for i in range(n):
            video_result = self.video_title_element  # Use self.video_title_element instead of self.video_title
            video_url = video_result.get_attribute("href")
            video_urls.append(video_url)

        print("URLs of the first {} videos:".format(n))
        for url in video_urls:
            print(url)

    def click_first_video(self):
        search_results = self._driver.find_elements(By.ID, self.VIDEO_TITLE_ID)

        for result in search_results:
            if self.search_query.lower() in result.text.lower():
                result.click()
                return

        # If no matching result is found, you may want to handle it accordingly (e.g., raise an exception)
        raise NoSuchElementException("No matching result found for the search query.")
