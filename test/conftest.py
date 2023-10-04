import pytest
import json
import selenium.webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['implicit_wait'] > 0
    print("Hello")
    return config


@pytest.fixture(scope='function')
def driver(config) -> WebDriver:
    # opts = selenium.webdriver.ChromeOptions()
    # opts.add_argument('headless')
    # webdriver = selenium.webdriver.Chrome(options=opts)
    print("Before test")
    webdriver = selenium.webdriver.Chrome()
    webdriver.implicitly_wait(config['implicit_wait'])
    yield webdriver
    print("After test")
    webdriver.quit()
