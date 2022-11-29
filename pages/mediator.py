from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base import Base

from data.other import ElementAttributes


class Mediator(Base):
    """Класс-посредник, содержащий общие методы."""

    element_by_text = "//*[text()='{}']"

    def advertisements_search(self, advertisements_name: str):
        """
        Совершает поиск по названию объявления.

        :param advertisements_name: Название объявления.
        """
        self.wait_element_located(By.ID, "downshift-input").send_keys(advertisements_name)
        self.get_element_by_attribute(ElementAttributes.marker, "search-form/submit-button").click()
        return self

    def click_by_text(self, element_text: str):
        """
        Нажимает на элемент.

        :param element_text: Текст элемента.
        """
        self.click(By.XPATH, self.element_by_text.format(element_text))
        return self

    def get_element_by_attribute(self,
                                 attribute_name: str,
                                 attribute_value: str
                                 ) -> WebElement:
        """
        Возвращает элемент по его аттрибуту.

        :param attribute_name: Название аттрибута.
        :param attribute_value: Значение аттрибута.
        """
        element_by_attribute = f"//*[@{attribute_name}='{attribute_value}']"
        return self.wait_element_located(By.XPATH, element_by_attribute)

    def check_elements_by_part_text(self, *elements_texts: str) -> True or TimeoutException:
        """
        Проверка отображения элементов по части текстового значения.

        :param elements_texts: Части текстовых значений элементов.
        """
        for element_text in elements_texts:
            self.wait_element_located(By.XPATH, f"//*[contains(text(), '{element_text}')]")
        return True

    def check_located_elements_by_text(self, *elements_texts: str) -> True or TimeoutException:
        """
        Проверка отображения элементов по текстовому значению.

        :param elements_texts: Текстовые значения элементов.
        """
        for element_text in elements_texts:
            self.wait_element_located(By.XPATH, self.element_by_text.format(element_text))
        return True

    def check_advt_displayed(self) -> bool:
        """Проверка отображения объявлений."""
        advertisements = self.find_elements(By.XPATH, f"//div[@{ElementAttributes.marker}='item']")

        if not advertisements:
            return False

        for advt in advertisements:
            if not advt.is_displayed():
                return False
        return True

    def add_favorites_first_advt(self):
        """Добавляет первое в списке объявление в избранное."""
        self.get_element_by_attribute(ElementAttributes.marker, "favorites-add").click()
        return self

    def get_first_advt_title(self) -> str:
        """Возвращает заголовок первого объявления."""
        return self.wait_element_located(By.XPATH, f"//a[@{ElementAttributes.marker}='item-title']/h3").text

    def open_favorites(self):
        """Открывает страницу с избранными товарами."""
        self.get_element_by_attribute(ElementAttributes.title, "Избранное").click()
        return self
