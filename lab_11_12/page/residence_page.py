from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from page.booking_page import BookingPage
from utils.loggers import PAGE_LOGGER
from time import sleep


class ResidencePage(PageFactory):
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.booking_button_locator = (
            By.XPATH, 
            "//div[@data-section-id='BOOK_IT_SIDEBAR']//button[@data-testid='homes-pdp-cta-btn']"
        )
        self.auto_translation_locators = {
            'auto_translation': (By.XPATH, "//button[@aria-labelledby='auto_translate_switch']"),
            'close_popup_button': (By.XPATH, "//button[@aria-label='Close']")
        }
        self.сzech_region_locator = (By.XPATH, "//a[@lang='cs-CZ']")
    

    locators = {
        'header': ('XPATH', "//h1[@tabindex='-1']"),
        'region_settings': ('XPATH', "//button[@aria-label='Choose a language and currency']"),
        'address': ('XPATH', "/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[2]/div[1]/span[5]/button/span")
    }


    def get_address(self) -> str:
        PAGE_LOGGER.debug('Get address')
        return self.address.text


    def get_header(self) -> str:
        PAGE_LOGGER.debug('Get header')
        return self.header.text


    def open(self, link: str):
        PAGE_LOGGER.info('Open residence page by link')
        self.driver.get(link)
        sleep(4)


    def open_booking_page(self) -> BookingPage:
        PAGE_LOGGER.info('Open booking page')
        print(self.driver.title)
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.booking_button_locator)) \
            .click()
        return BookingPage(self.driver)
    

    def switch_auto_translation(self):
        PAGE_LOGGER.info("Switch automatic translation")
        self.region_settings.click()
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.auto_translation_locators['auto_translation'])) \
            .click()
        sleep(4)


    def close_auto_translation_popup(self):
        PAGE_LOGGER.debug('Close automatic translation popup')
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.auto_translation_locators['close_popup_button'])) \
            .click()
    

    def set_region_сzech(self):
        PAGE_LOGGER.info("Set region 'Czech'")
        self.region_settings.click()
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.сzech_region_locator)) \
            .click()
        sleep(3)
