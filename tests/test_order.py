import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import BASE_URL
from data.order_data import ORDER_DATA_SETS


@allure.epic("Самокат")
@allure.feature("Заказ")
@pytest.mark.order
class TestOrder:

    @allure.title("Позитивный заказ самоката через верхнюю кнопку")
    def test_order_flow_top_button(self, driver, wait):
        main = MainPage(driver, wait)
        order = OrderPage(driver, wait)

        main.open(BASE_URL)
        main.accept_cookies()
        main.click_order_top()

        order.fill_step_one(ORDER_DATA_SETS[0])
        order.fill_step_two_black(ORDER_DATA_SETS[0])
        order.submit_order()
        order.assert_success()

    @allure.title("Позитивный заказ самоката через нижнюю кнопку")
    def test_order_flow_bottom_button(self, driver, wait):
        main = MainPage(driver, wait)
        order = OrderPage(driver, wait)

        main.open(BASE_URL)
        main.accept_cookies()
        main.click_order_bottom()

        order.fill_step_one(ORDER_DATA_SETS[1])
        order.fill_step_two_grey(ORDER_DATA_SETS[1])
        order.submit_order()
        order.assert_success()