from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.labirint.ru/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window

    def set_cokie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }
        self._driver.add_cookie(cookie) 
        print('меня вызвали')

    def serch(self, tern):
        self._driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(tern)
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()