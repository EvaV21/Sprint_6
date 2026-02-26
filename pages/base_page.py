import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step("Открыть страницу: {url}")
    def open(self, url: str):
        self.driver.get(url)

    @allure.step("Клик по элементу")
    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    @allure.step("Безопасный клик (JS)")
    def js_click(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", el)

    @allure.step("Ввести текст")
    def type(self, locator, text: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    @allure.step("Получить текст")
    def get_text(self, locator) -> str:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    @allure.step("Элемент видим")
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Переключиться на последнюю вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Получить текущий URL")
    def current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Ждать URL = {url}")
    def wait_url_to_be(self, url: str):
        self.wait.until(EC.url_to_be(url))

    @allure.step("Ждать URL содержит: {part}")
    def wait_url_contains(self, part: str):
        self.wait.until(lambda d: part in d.current_url)

    @allure.step("Принять cookies, если баннер есть")
    def accept_cookies_if_present(self, locator, timeout=3):
        try:
            from selenium.webdriver.support.ui import WebDriverWait
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            pass
    @allure.step("Ждать количество вкладок: {count}")
    def wait_number_of_windows(self, count: int):
        self.wait.until(EC.number_of_windows_to_be(count))

    @allure.step("Открыть URL в текущей вкладке: {url}")
    def go_to(self, url: str):
        self.driver.get(url)