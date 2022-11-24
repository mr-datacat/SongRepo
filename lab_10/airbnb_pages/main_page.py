from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from residence_page import ResidencePage
from time import sleep


class MainPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.first_residence_locator = (By.XPATH, "(//div/a[@tabindex='-1'])[1]")
        self.close_popup_button_locator = (By.XPATH, "//button[@aria-label='Закрыть']")
        self.first_map_house_locator = (By.XPATH, "(//button[@data-veloute='map/markers/BasePillMarker'])[1]")
        self.first_map_house_block_locator = (By.XPATH, "(//div[contains(@aria-labelledby, 'title')])[1]")
        self.first_map_house_link_locator = (By.XPATH, "(//a[contains(@aria-labelledby, 'title')])[1]")
        self.map_button_locator = (By.XPATH, "//span[text()='Показать карту']")

    def open(self):
        self.driver.get('https://www.airbnb.ru/?enable_auto_translate=false&display_currency=EUR')
        sleep(4)
        self.close_popup()
    
    def show_map(self):
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.map_button_locator)).click()

    def click_first_map_house(self):
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.first_map_house_locator)).click()

    def get_first_map_house_link_value(self) -> str:
        link = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.first_map_house_link_locator))
        return link.get_attribute("href")
    
    def open_first_map_house_page(self) -> ResidencePage:
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.first_map_house_block_locator)).click()
        return ResidencePage(self.driver)
    
    def close_popup(self):
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.close_popup_button_locator)).click()
