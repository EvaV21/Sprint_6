import allure
from pages.base_page import BasePage
import locators.main_page_locators as L

class MainPage(BasePage):

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.accept_cookies_if_present(L.COOKIE_BUTTON)

    @allure.step("Нажать кнопку Заказать (верхняя)")
    def click_order_top(self):
        self.click(L.ORDER_TOP)

    @allure.step("Нажать кнопку Заказать (нижняя)")
    def click_order_bottom(self):
        self.click(L.ORDER_BOTTOM)

    @allure.step("Нажать лого Самокат")
    def click_scooter_logo(self):
        self.click(L.SCOOTER_LOGO)

    @allure.step("Нажать лого Яндекс")
    def click_yandex_logo(self):
        self.click(L.YANDEX_LOGO)

    @allure.step("Открыть вопрос FAQ #{i}")
    def open_faq_question(self, i: int):
        self.accept_cookies()          # ← добавить
        self.js_click(L.FAQ_QUESTION(i))  # ← лучше js_click, чтобы не ловить перехват

    @allure.step("Получить ответ FAQ #{i}")
    def get_faq_answer(self, i: int) -> str:
        return self.get_text(L.FAQ_ANSWER(i))