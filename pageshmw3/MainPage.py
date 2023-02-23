from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window
        serch_input = driver.find_element(By.CSS_SELECTOR, "input#user-name")
        serch_input.send_keys("standard_user")
        serch_input = driver.find_element(By.CSS_SELECTOR, "input#password")
        serch_input.send_keys("secret_sauce")