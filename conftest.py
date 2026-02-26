import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Choose browser: firefox or chrome"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "firefox":
        options = FirefoxOptions()
        service = FirefoxService()  
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "chrome":
        options = ChromeOptions()
        service = ChromeService() 
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError("Browser not supported. Use --browser=firefox or --browser=chrome")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)