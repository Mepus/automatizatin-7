from selenium.webdriver.common.by import By
class Register:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    def input_field(self,locator:str, txt:str):
        self._driver.find_element(By.CSS_SELECTOR, locator).click()
        el = self._driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
        return el