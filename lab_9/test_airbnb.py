import unittest
from selenium import webdriver
from airbnb_pages.main_page import MainPage

class TestAirbnb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_case_2(self):
        main_page = MainPage(self.driver)
        main_page.open()
        residence_page = main_page.open_first_residence()
        self.driver.switch_to.window(self.driver.window_handles[1])
        booking_page = residence_page.open_booking_page()
        USD_price = booking_page.get_price()
        booking_page.set_currency_PLN()
        PLN_price = booking_page.get_price()
        print(USD_price)
        print(PLN_price)
        self.assertTrue(USD_price != PLN_price)
    
    def tearDown(self):
        self.driver.quit()
        pass