import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
import locators.order_page_locators as L


class OrderPage(BasePage):

    @allure.step("Заполнить шаг 1 формы заказа")
    def fill_step_one(self, data: dict):
        self.type(L.NAME, data["name"])
        self.type(L.SURNAME, data["surname"])
        self.type(L.ADDRESS, data["address"])

        self.click(L.METRO)
        self.type(L.METRO, data["metro"])

        options = self.wait.until(EC.visibility_of_all_elements_located(L.METRO_DROPDOWN_OPTIONS))
        options[0].click()

        self.type(L.PHONE, data["phone"])
        self.click(L.NEXT)

        self.is_visible(L.DATE)

    @allure.step("Выбрать дату доставки: {date}")
    def set_date(self, date: str):
        date_input = self.wait.until(EC.element_to_be_clickable(L.DATE))
        date_input.click()
        date_input.send_keys(Keys.CONTROL, "a")
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {rent_period}")
    def set_rent_period(self, rent_period: str):
        self.click(L.RENT_CONTROL)
        self.is_visible(L.RENT_MENU)
        self.click(L.RENT_OPTION_XPATH(rent_period))

    @allure.step("Выбрать цвет: черный жемчуг")
    def choose_black_color(self):
        self.click(L.COLOR_BLACK)

    @allure.step("Выбрать цвет: серая безысходность")
    def choose_grey_color(self):
        self.click(L.COLOR_GREY)

    @allure.step("Ввести комментарий")
    def set_comment(self, comment: str):
        self.type(L.COMMENT, comment)

    @allure.step("Заполнить шаг 2 формы заказа (черный)")
    def fill_step_two_black(self, data: dict):
        self.set_date(data["date"])
        self.set_rent_period(data["rent_period"])
        self.choose_black_color()
        self.set_comment(data["comment"])

    @allure.step("Заполнить шаг 2 формы заказа (серый)")
    def fill_step_two_grey(self, data: dict):
        self.set_date(data["date"])
        self.set_rent_period(data["rent_period"])
        self.choose_grey_color()
        self.set_comment(data["comment"])

    @allure.step("Отправить заказ и подтвердить")
    def submit_order(self):
        self.js_click(L.ORDER_BUTTON)
        self.is_visible(L.CONFIRM_YES)
        self.js_click(L.CONFIRM_YES)

    @allure.step("Проверить успешное оформление заказа")
    def assert_success(self):
        self.is_visible(L.SUCCESS_MODAL)
        self.is_visible(L.SUCCESS_TEXT)