from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:

    RESULT_TITLE = (By.XPATH, "//div[@data-testid='about']//h2")

    def __init__(self, driver):
        self.driver = driver

    def title(self, desired_text):
        explicit_wait = WebDriverWait(self.driver, 10)
        explicit_wait.until(EC.title_contains(desired_text))
        fluent_wait = WebDriverWait(self.driver, 10, 1, ignored_exceptions=[Exception])
        fluent_wait.until(text_contains(self.RESULT_TITLE, desired_text))
        return self.driver.find_element(*self.RESULT_TITLE).text

class text_contains(object):

  def __init__(self, locator, desired_text):
    self.locator = locator
    self.desired_text = desired_text

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.desired_text in element.text:
        return element
    else:
        return False
