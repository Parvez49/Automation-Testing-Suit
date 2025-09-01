import pytest
from selenium.webdriver.common.by import By

from utils.browser_factory import get_browser


@pytest.fixture
def driver():
    driver = get_browser("firefox")
    yield driver
    driver.quit()


def test_login(driver):
    driver.get("https://www.saucedemo.com/")  # demo e-commerce site
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url

    driver.quit()
