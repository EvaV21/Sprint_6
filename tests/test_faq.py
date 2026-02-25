import pytest
import allure
from pages.main_page import MainPage
from data.urls import BASE_URL


FAQ_CASES = [
    (0, "Сутки — 400 рублей"),
    (1, "Пока что у нас так"),
    (2, "Допустим, вы оформляете заказ"),
    (3, "Только начиная с завтрашнего дня"),
    (4, "Пока что нет"),
    (5, "Самокат приезжает к вам"),
    (6, "Штрафа не будет"),
    (7, "Московской области"),
]


@allure.epic("Самокат")
@allure.feature("FAQ")
@pytest.mark.faq
class TestFAQ:

    @allure.title("Проверка ответа FAQ")
    @pytest.mark.parametrize("index, expected_part", FAQ_CASES)
    def test_faq_answer_opens(self, driver, wait, index, expected_part):
        page = MainPage(driver, wait)
        page.open(BASE_URL)

        page.open_faq_question(index)
        answer = page.get_faq_answer(index)

        assert expected_part in answer