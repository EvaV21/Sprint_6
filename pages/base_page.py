import allure
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step("Открыть страницу: {url}")
    def open(self, url: str):
        self.driver.get(url)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        self.driver.execute_script("arguments[0].click();", el)

    def type(self, locator, value: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    def get_text(self, locator) -> str:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def is_visible(self, locator) -> bool:
        self.wait.until(EC.visibility_of_element_located(locator))
        return True