from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pageshmw.RegisterPage import Register
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))




@pytest.mark.parametrize("locator, data", ["[name='first-name']", "Иван"])
def test_fill_field_first_name(locator, data):
    registrated = Register()
    registrated.input_first_name(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='last-name']", "Петров"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_last_name(locator, data)


@pytest.mark.parametrize("locator, data", ["[name='address']", "Ленина, 55-3"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_address(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='zip-code']", "", "#zip-code"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_zip_code(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='city']", "Москва"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_city(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='country']", "Россия"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_country(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='job-position']", "QA"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_job_position(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='company']", "SkyPro"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_company(locator, data)