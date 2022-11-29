import pytest
from selenium import webdriver

from pages.main import MainPage
from pages.work import WorkPage

from data.other import Routes
from data.search import Categories


@pytest.fixture
def driver():
    """Инициализирует веб-драйвер браузера."""
    driver = webdriver.Chrome()
    driver.get(Routes.url)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    """Предоставляет объект для работы с главной страницей."""
    return MainPage(driver)


@pytest.fixture
def work_page(main_page):
    """Предоставляет объект для работы со страницей 'Работа' и соответствующее состояние веб-драйвера."""
    main_page.choose_category(Categories.work)
    return WorkPage(main_page.driver)
