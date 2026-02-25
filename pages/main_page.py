import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class MainPage(BasePage):
    ORDER_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g")
    ORDER_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button")

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")

    @staticmethod
    def FAQ_QUESTION(i: int):
        return (By.ID, f"accordion__heading-{i}")

    @staticmethod
    def FAQ_ANSWER(i: int):
        return (By.ID, f"accordion__panel-{i}")

    @allure.step("Принять cookies, если баннер есть")
    def accept_cookies_if_present(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except TimeoutException:
            pass

    @allure.step("Открыть вопрос FAQ #{i}")
    def open_faq_question(self, i: int):
        self.click(self.FAQ_QUESTION(i))

    @allure.step("Получить ответ FAQ #{i}")
    def get_faq_answer(self, i: int) -> str:
        return self.get_text(self.FAQ_ANSWER(i))

    def click_order_top(self):
        self.click(self.ORDER_TOP)

    def click_order_bottom(self):
        self.click(self.ORDER_BOTTOM)

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)