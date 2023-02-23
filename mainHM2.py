import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageshm2.Calculator import MainPage

def test_cart_counter():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = MainPage(driver)
sleep(45)

@pytest.mark.parametrize( 'locator',[('.screen')])

def test_result(locator):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    assert driver.find_element(By.CSS_SELECTOR, locator).text == "15"
    driver.quit()