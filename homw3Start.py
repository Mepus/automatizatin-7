from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageshmw3.MainPage import MainPage

def test_cart_counter():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.send_keys('standard_user')
    main_page.send_keys("secret_sauce")


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
serch_input = driver.find_element(By.CSS_SELECTOR, "input#login-button")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#checkout").click()

sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "input#first-name")
serch_input.send_keys("Бичико")
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "input#last-name")
serch_input.send_keys("Мепуришвили")
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "input#postal-code")
serch_input.send_keys("146326382")
sleep(2)
serch_input = driver.quit()




