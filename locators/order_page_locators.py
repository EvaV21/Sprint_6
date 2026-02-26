from selenium.webdriver.common.by import By

NAME = (By.XPATH, "//input[@placeholder='* Имя']")
SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
NEXT = (By.XPATH, "//button[text()='Далее']")

METRO_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, ".select-search__select .select-search__option")

DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

RENT_CONTROL = (By.CSS_SELECTOR, "div.Dropdown-root .Dropdown-control")
RENT_MENU = (By.CSS_SELECTOR, "div.Dropdown-root.is-open .Dropdown-menu")
RENT_OPTIONS = (By.CSS_SELECTOR, "div.Dropdown-root.is-open .Dropdown-option")

COLOR_BLACK = (By.ID, "black")
COLOR_GREY = (By.ID, "grey")

COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[contains(.,'Заказать')]")
CONFIRM_YES = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[normalize-space()='Да']")

SUCCESS_MODAL = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
SUCCESS_TEXT = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")

def RENT_OPTION_XPATH(text: str):
    return (By.XPATH, f"//div[contains(@class,'Dropdown-option')][normalize-space()='{text}']")