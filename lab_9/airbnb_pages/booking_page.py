from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

class BookingPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.currency_button_locator = (By.ID, "MowebCurrencyPicker_trigger")
        self.PLN_currency_locator = (By.XPATH, "//div[@data-value='PLN']")
        self.price_locator = (By.XPATH, "//div[@data-testid='price-item-total']/span")

    def set_currency_PLN(self):
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.currency_button_locator)).click()
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.PLN_currency_locator)).click()
        sleep(7)

    def get_price(self) -> float:
        raw_price_element = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.price_locator))
        raw_price = raw_price_element.text
        price_string = ''
        for char in raw_price:
            if char.isdigit():
                price_string += char
            elif char == ',':
                price_string += '.'
        return float(price_string)
