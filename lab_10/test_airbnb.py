import unittest
from selenium import webdriver
from airbnb_pages.main_page import MainPage
from time import sleep

class TestAirbnb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_case_10(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.show_map()
        main_page.click_first_map_house()
        first_map_house_link_value = main_page.get_first_map_house_link_value().partition('?')[0]
        main_page.open_first_map_house_page()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url_value = str(self.driver.current_url).partition('?')[0]
        self.assertTrue(first_map_house_link_value == current_url_value)
    
    def tearDown(self):
        self.driver.quit()
        pass