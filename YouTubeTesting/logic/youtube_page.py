from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
from infra.base_page import BasePage

class YouTubePage(BasePage):

    # Home page Related
    SEARCH_INPUT = "//input[@id='search']"
    MENU_ICON = '//*[@id="guide-button"]'

    # podcast related
    PODCASTS_BUTTON = "//a[@title='Podcasts']"
    POPULAR_EPISODES = "@id='title' and contains(@class, 'style-scope ytd-shelf-renderer') and text()='Popular episodes']"

    MUSIC_BUTTON = "//a[@title='Music']"
    MUSIC_PLAYLIST = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[2]/div/ytd-compact-station-renderer[1]/div/a"

    # Shorts related
    SHORTS_BUTTON = "//a[@title='Shorts']"
    SHORTS_DOWN_BUTTON = '//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]'
    SHORTS_COMMENTS = '//*[@id="comments-button"]/ytd-button-renderer/yt-button-shape/label/button/yt-touch-feedback-shape/div/div[2]'
    SHORTS_CHANNEL = "//div[@id='container' and contains(@class, 'ytd-channel-name')]//yt-formatted-string/a"
    SHORTS_MUTE_BUTTON = '//button[@aria-label="Mute (m)"]'

    FILTER_SEARCH = '//*[@id="filter-button"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]'

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self.shorts_button = self._driver.find_element(By.XPATH, self.SHORTS_BUTTON)




    def fill_search_input(self, title):
        self.search_input.send_keys(title)

    def press_on_enter_search(self):
        self.search_input.send_keys(Keys.RETURN)  # logic

    def press_on_filter(self):
        self.filter = self._driver.find_element(By.XPATH,self.FILTER_SEARCH)
        self.filter.click()

    def go_to_shorts(self):
        self.shorts_button.click()

    def open_menu(self):
        print('in open menu')
        self.menu_icon = self._driver.find_element(By.XPATH,self.MENU_ICON)
        self.menu_icon.click()

    def go_to_podcasts(self):
        self.podcasts_button = self._driver.find_element(By.XPATH,self.PODCASTS_BUTTON)
        self.podcasts_button.click()

    def go_to_podcasts_popular_episodes(self):
        self.popular_podcasts = self._driver.find_element(By.XPATH,self.POPULAR_EPISODES)
        self.popular_podcasts.click()

    def go_to_youtube_music(self):
        self.music_button = self._driver.find_element(By.XPATH,self.MUSIC_BUTTON)
        self.music_button.click()

    def go_to_playlist(self):
        self.playlist = self._driver.find_element(By.XPATH,self.MUSIC_PLAYLIST)
        link = self.playlist.get_attribute("href")
        self._driver.get(link)


    def scroll_shorts(self):
        self.shorts_down_button = self._driver.find_element(By.XPATH, self.SHORTS_DOWN_BUTTON)
        self.shorts_down_button.click()

    def shorts_comments(self):
        self.shorts_comments = self._driver.find_element(By.XPATH, self.SHORTS_COMMENTS)
        self.shorts_comments.click()

    def mute_short(self):
        self.short_mute_button = self._driver.find_element(By.XPATH,self.SHORTS_MUTE_BUTTON)
        self.short_mute_button.click()

    def shorts_Channel(self):
        # Wait for the Shorts channel link to be clickable
        shorts_channel_link = self._driver.find_element(By.XPATH, self.SHORTS_CHANNEL)

        # Click on the Shorts channel link
        shorts_channel_link.click()

    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        return WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable((by, value)))


    def search_flow(self, text):
        print('in search flow')
        self.fill_search_input(text)
        self.press_on_enter_search()
