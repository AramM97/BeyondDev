import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys

from infra.base_page import BasePage


class YoutubeVideoPage(BasePage):
    COMMENTS = '//*[@id="content-text"]'
    FULL_SCREEN_BUTTON = '//*[@id="movie_player"]/div[37]/div[2]/div[2]/button[9]'

    def __init__(self, driver):
        super().__init__(driver)
        print('YoutubeVideoPage constructor start')
        time.sleep(5)

        #self.full_screen_button = self._driver.find_element(By.XPATH, self.FULL_SCREEN_BUTTON)

        #self.comments_element = self._driver.find_element(By.XPATH, self.COMMENTS)
        self.full_screen_button = self._driver.find_element(By.XPATH, self.FULL_SCREEN_BUTTON)
        print('finished')
        #self.all_comments = [elem.text for elem in self.comments_element]


       # try:
       #     # Wait for the comments section to load
        #    WebDriverWait(self._driver, 10).until(
        #        EC.presence_of_element_located((By.XPATH, self.COMMENTS)))
         #   print('Comments section loaded')

            # Then, wait for the pinned comment element to load
           # WebDriverWait(self._driver, 10).until(
           #     EC.presence_of_element_located((By.XPATH, self.COMMENTS)))
            #print('Pinned comment element loaded')

            # Continue with the rest of the constructor
            #time.sleep(2)
            #self.pinned_comment_element = self._driver.find_element(By.XPATH, self.COMMENTS)
            #print('Finish construct')


       # except Exception as e:
        #    print(f'Error in constructor: {str(e)}')
         #   raise  # Re-raise the exception to see the full traceback

    def get_pinned_comment(self):
        print('in get comment')
        pinned_comment_text = ""
        # Extract the text of the pinned comment
        #pinned_comment_text = self.pinned_comment_element.text
        for comment in self.all_comments:
            if "Pinned" in comment:
                pinned_comment_text = comment


        return pinned_comment_text

    def make_video_full_screen(self):
        # Send the 'f' key to make the video full screen
        self._driver.find_element(By.XPATH, self.FULL_SCREEN_BUTTON).send_keys(Keys.F)