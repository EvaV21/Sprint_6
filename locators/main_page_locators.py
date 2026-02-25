from selenium.webdriver.common.by import By

ORDER_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g")
ORDER_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button")

COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")

def FAQ_QUESTION(i: int):
    return (By.ID, f"accordion__heading-{i}")

def FAQ_ANSWER(i: int):
    return (By.ID, f"accordion__panel-{i}")