from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


class SearchPage:

    URL = "https://duckduckgo.com/"

    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def search(self, text):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(text)
        time.sleep(1)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
