import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import BASE_URL
from data.order_data import ORDER_DATA_SETS

@allure.epic("Самокат")
@allure.feature("Заказ")
@pytest.mark.order
class TestOrder:
    @pytest.mark.parametrize("entry, data", [
        ("top", ORDER_DATA_SETS[0]),
        ("bottom", ORDER_DATA_SETS[1]),
    ])
    def test_order_flow_positive(self, driver, wait, entry, data):
        main = MainPage(driver, wait)
        order = OrderPage(driver, wait)

        main.open(BASE_URL)
        main.accept_cookies_if_present()

        if entry == "top":
            main.click_order_top()
        else:
            main.click_order_bottom()

        order.fill_step_one(data)
        order.fill_step_two(data)
        order.submit_order()
        order.assert_success()