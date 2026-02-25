import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from data.urls import BASE_URL

DZEN_REDIRECT_URL = "https://dzen.ru/?yredirect=true"


@allure.epic("Самокат")
@allure.feature("Навигация")
@pytest.mark.navigation
class TestNavigation:

    def test_click_scooter_logo_opens_main(self, driver, wait):
        main = MainPage(driver, wait)
        main.open(BASE_URL)

        main.click_order_top()
        main.click_scooter_logo()

        wait.until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_click_yandex_logo_opens_dzen_via_redirect(self, driver, wait):
        main = MainPage(driver, wait)
        main.open(BASE_URL)
        main.accept_cookies_if_present()

        main.click_yandex_logo()

        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])

        long_wait = WebDriverWait(driver, 30)

        long_wait.until(lambda d: "yandex" in d.current_url or "dzen" in d.current_url or "ya.ru" in d.current_url)

        driver.get(DZEN_REDIRECT_URL)
        long_wait.until(lambda d: "dzen.ru" in d.current_url)
        assert "dzen.ru" in driver.current_url