from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cookie = {
    "name": "cookie_policy",
    "value": "1"
}

def test_cart_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window
    browser.add_cookie(cookie)


    # найти все книги по слову python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    # переключиться на таблицу
    browser.find_element(By.CSS_SELECTOR, "a[title=таблицей]").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located( (By.CSS_SELECTOR, "table") )
    )

    # добавить все книги в корзину и посчитать, сколько
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
        
    # перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

    # проверить счетчик товаров. Должен быть равен числу нажатий
        # получить текущее значение

    a = browser.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]')
    txt = a.find_element(By.CSS_SELECTOR, "b").text
        # сранить с counter
    assert counter == int(txt)

    

    browser.quit()





