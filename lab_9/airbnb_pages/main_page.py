from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from airbnb_pages.residence_page import ResidencePage
from time import sleep


class MainPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.first_residence_locator = (By.XPATH, "(//div/a[@tabindex='-1'])[1]")

    def open(self):
        self.driver.get('https://www.airbnb.ru/?enable_auto_translate=false&display_currency=EUR')
        sleep(7)

    def open_first_residence(self) -> ResidencePage:
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.first_residence_locator)).click()
        return ResidencePage(self.driver)
