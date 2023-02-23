from time import sleep
from selenium.webdriver.common.by import By
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window

    def Calk(self):
        
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys(45)
        sleep(2)

        self._driver.find_element(By.XPATH, '//*[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//*[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//*[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//*[text()="="]').click()
        sleep(45)
