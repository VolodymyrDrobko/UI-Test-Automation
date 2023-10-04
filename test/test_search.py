from page.result_page import ResultPage
from page.search_page import SearchPage
from test.conftest import driver


def test_search(driver):
    search_page = SearchPage(driver)
    result_page = ResultPage(driver)

    text = "Giant panda"

    search_page.load()
    search_page.search(text)

    assert text in result_page.title(text)


def test_example(driver):
    print("Second")
