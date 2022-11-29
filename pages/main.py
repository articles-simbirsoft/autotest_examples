from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.mediator import Mediator

from data.search import Categories


class MainPage(Mediator):
    """Предоставляет функционал для работы с главной страницей."""

    category_locator = "//a[text()='{}'][@class]"

    def check_categories(self) -> True or TimeoutException:
        """Проверка отображения списка категорий объявлений."""
        for category in Categories().get_all_values():
            self.wait_element_located(By.XPATH, self.category_locator.format(category))
        return True

    def choose_category(self, category: str):
        """
        Нажимает на категорию объявлений.

        :param category: Название категории.
        """
        self.click(By.XPATH, self.category_locator.format(category))
        return self
