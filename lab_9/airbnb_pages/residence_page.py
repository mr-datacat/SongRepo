from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from airbnb_pages.booking_page import BookingPage

class ResidencePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.booking_button_locator = (
            By.XPATH, 
            "//div[@data-section-id='BOOK_IT_SIDEBAR']//button[@data-testid='homes-pdp-cta-btn']"
        )

    def open_booking_page(self):
        print(self.driver.title)
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.booking_button_locator)).click()
        return BookingPage(self.driver)
