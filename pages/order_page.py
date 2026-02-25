from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import allure
from pages.base_page import BasePage


class OrderPage(BasePage):
    # Шаг 1
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT = (By.XPATH, "//button[text()='Далее']")

    # Метро: варианты в выпадашке
    METRO_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, ".select-search__select .select-search__option")

    # Шаг 2
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # Срок аренды (Dropdown)
    RENT_ROOT = (By.CSS_SELECTOR, "div.Dropdown-root")
    RENT_CONTROL = (By.CSS_SELECTOR, "div.Dropdown-root .Dropdown-control")
    RENT_MENU = (By.CSS_SELECTOR, "div.Dropdown-root.is-open .Dropdown-menu")
    RENT_OPTIONS = (By.CSS_SELECTOR, "div.Dropdown-root.is-open .Dropdown-option")

    # Цвет
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка заказать и подтверждение
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[contains(.,'Заказать')]")
    CONFIRM_YES = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[normalize-space()='Да']")

    # Успех
    SUCCESS_MODAL = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")

    @staticmethod
    def RENT_OPTION_XPATH(text: str):
        # пункты типа "сутки", "двое суток" и т.п.
        return (By.XPATH, f"//div[contains(@class,'Dropdown-option')][normalize-space()='{text}']")

    # ----------------- helpers -----------------

    def _scroll_into_view(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    def _js_click(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", el)

    def _safe_click(self, locator):
        """Обычный клик, если не вышло — JS-клик (часто спасает Firefox + overlay)."""
        try:
            el = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            el.click()
        except Exception:
            self._js_click(locator)

    # ----------------- steps -----------------

    @allure.step("Заполнить шаг 1 формы заказа")
    def fill_step_one(self, data: dict):
        self.type(self.NAME, data["name"])
        self.type(self.SURNAME, data["surname"])
        self.type(self.ADDRESS, data["address"])

        # метро
        self._safe_click(self.METRO)
        self.type(self.METRO, data["metro"])

        # ждём варианты и кликаем по первому (самый стабильный вариант)
        options = self.wait.until(EC.visibility_of_all_elements_located(self.METRO_DROPDOWN_OPTIONS))
        options[0].click()

        self.type(self.PHONE, data["phone"])
        self._safe_click(self.NEXT)

        # ждём, что появился шаг 2
        self.wait.until(EC.visibility_of_element_located(self.DATE))

    @allure.step("Заполнить шаг 2 формы заказа")
    def fill_step_two(self, data: dict):
        # дата: вводим и закрываем календарь Enter-ом
        date_input = self.wait.until(EC.element_to_be_clickable(self.DATE))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_input)
        date_input.click()
        date_input.send_keys(Keys.CONTROL, "a")
        date_input.send_keys(data["date"])
        date_input.send_keys(Keys.ENTER)

        # клик в пустое место, чтобы календарь точно закрылся
        self.driver.find_element(By.TAG_NAME, "body").click()

        # срок аренды: открываем dropdown надёжно (scroll + safe/js click)
        self._scroll_into_view(self.RENT_CONTROL)
        self._safe_click(self.RENT_CONTROL)

        # ждём, что dropdown реально открылся
        self.wait.until(EC.visibility_of_element_located(self.RENT_MENU))

        # кликаем нужный пункт
        try:
            self._safe_click(self.RENT_OPTION_XPATH(data["rent_period"]))
        except TimeoutException:
            # запасной вариант: если текст чуть отличается — берём первый видимый пункт
            options = self.wait.until(EC.visibility_of_all_elements_located(self.RENT_OPTIONS))
            options[0].click()

        # цвет
        if data["color"] == "black":
            self._safe_click(self.COLOR_BLACK)
        else:
            self._safe_click(self.COLOR_GREY)

        self.type(self.COMMENT, data["comment"])

    @allure.step("Отправить заказ и подтвердить")
    def submit_order(self):
        # кнопка "Заказать"
        self._scroll_into_view(self.ORDER_BUTTON)
        self._safe_click(self.ORDER_BUTTON)

        # ждём модалку и жмём "Да"
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_YES))
        self._safe_click(self.CONFIRM_YES)

    @allure.step("Проверить успешное оформление заказа")
    def assert_success(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL))
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TEXT))