import time

from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class MainPage(BasePage):

    ACCEPT_COOKIES_BUTTON = "// button[ @ id = 'didomi-notice-agree-button']"
    DROP_DOWN_ARROW = "//div[@Class='dropdown_arrow_down__WqO5K']"

    TENNIS_MENU_ITEM = "/html/body/div[3]/div/header/div/div/div[1]/div[1]/div[3]/div/div[3]/a[2]"
    GAME_PAGE_BUTTON = "//a[@Class='featured-games-widget_button__qTjA1']"
    EXIT_POPUP_BUTTON = "//button[@class='popup_button__zfc0e']"

    MATCH_TIMER = "//div[@class='countdown_container__pfnWt countdown_small_view__3mGIF']"

    LIVE_SLIDER = "//div[@class='switch-button-content switch-text-button-content false main-header-module-mobile-button-content']"

    SEARCH_BUTTON = "//img[@class='main-header-module-mobile-buttons-search-icon']"
    SEARCH_INPUT = "//input[@class='main-header-module-mobile-input']"

    FEATURED_GAME_PAGE_ICON = "//a[@class='featured-games-widget_button__qTjA1']"



    def __init__(self, driver):
        super().__init__(driver)
        self.accept_cookies_button = self._driver.find_element(By.XPATH, self.ACCEPT_COOKIES_BUTTON)
        self.accept_cookies()
        self.drop_down_arrow = self._driver.find_element(By.XPATH, self.DROP_DOWN_ARROW)
        self.math_timer = self._driver.find_element(By.XPATH, self.MATCH_TIMER)
        self.live_view_slider = self._driver.find_element(By.XPATH, self.LIVE_SLIDER)
        self.search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
        self.featured_game_page_button = self._driver.find_element(By.XPATH, self.FEATURED_GAME_PAGE_ICON)





    def accept_cookies(self):
        self.accept_cookies_button.click()

    def exit_pop_up(self):
        time.sleep(10)
        self.exit_pop_up_button = self._driver.find_element(By.XPATH,self.EXIT_POPUP_BUTTON)
        self.exit_pop_up_button.click()

    def switch_to_tennis_scores(self):
        self.drop_down_arrow.click()
        self.tennis_menu_item = self._driver.find_element(By.XPATH, self.TENNIS_MENU_ITEM)
        self.tennis_menu_item.click()

    def get_match_timer(self):
        timer_text = self.math_timer.text
        print("Text from the div:", timer_text)
        return timer_text

    def switch_to_live_view(self):
        self.live_view_slider.click()

    def click_search_button(self):
        self.search_button.click()

    def search(self, text):
        self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self.search_input.send_keys(text)

    def enter_search(self):
        self.search_input.send_keys(Keys.RETURN)

    def search_flow(self, text):
        self.click_search_button()
        time.sleep(1)
        self.search(text)
        self.enter_search()

    def go_to_featured_game_page(self):
        self.feat_game_text = self.featured_game_page_button.text
        print(self.feat_game_text)
        if (self.feat_game_text == "עמוד משחק"):
            self.featured_game_page_button.click()





