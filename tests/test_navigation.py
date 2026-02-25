import allure
import pytest

from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from data.urls import BASE_URL, DZEN_REDIRECT_URL, DZEN_HOST


@allure.epic("Самокат")
@allure.feature("Навигация")
@pytest.mark.navigation
class TestNavigation:

    @allure.title("Клик по лого Самокат возвращает на главную")
    def test_click_scooter_logo_opens_main(self, driver, wait):
        main = MainPage(driver, wait)

        main.open(BASE_URL)
        main.accept_cookies()
        main.click_order_top()
        main.click_scooter_logo()

        main.wait_url_to_be(BASE_URL)
        assert main.current_url() == BASE_URL

    @allure.title("Клик по лого Яндекс открывает Дзен (через редирект)")
    def test_click_yandex_logo_opens_dzen_via_redirect(self, driver, wait):
        main = MainPage(driver, wait)
        dzen = DzenPage(driver, wait)

        main.open(BASE_URL)
        main.accept_cookies()
        main.click_yandex_logo()

        main.wait_number_of_windows(2)
        dzen.switch_to_new_tab()

        # принудительно уводим на стабильный редирект
        dzen.go_to(DZEN_REDIRECT_URL)
        dzen.wait_url_contains(DZEN_HOST)

        assert DZEN_HOST in dzen.current_url()