import pytest
import allure
from pages.main_page import MainPage
from data.urls import BASE_URL
from data.faq_data import FAQ_CASES


@allure.epic("Самокат")
@allure.feature("FAQ")
@allure.title("Проверка ответов в FAQ")
@pytest.mark.faq
class TestFAQ:

    @allure.title("Проверка ответа FAQ")
    @pytest.mark.parametrize("index, expected_part", FAQ_CASES)
    def test_faq_answer_opens(self, driver, wait, index, expected_part):
        page = MainPage(driver, wait)
        page.open(BASE_URL)

        page.accept_cookies()  #
        page.open_faq_question(index)
        answer = page.get_faq_answer(index)

        assert expected_part in answer