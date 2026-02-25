# Sprint_6


## Описание проекта
В проекте реализованы UI-автотесты для сервиса аренды самокатов.

Покрыты следующие сценарии:
- FAQ (раскрытие вопросов и проверка ответов)
- Навигация (логотип Самоката и Яндекса)
- Позитивный сценарий оформления заказа (через верхнюю и нижнюю кнопки)

Тесты написаны с использованием:
- Python
- Pytest
- Selenium WebDriver
- Allure Report
 
 ## Структура проекта

 Sprint_6/

tests/               # тесты
pages/               # Page Object классы
data/                # тестовые данные и URL
allure-report/       # сгенерированный отчёт
conftest.py          # фикстуры pytest
requirements.txt     # зависимости
README.md

## Как запустить проект

pytest -v --alluredir=allure_results

### Установить зависимости

bash
pip install -r requirements.txt