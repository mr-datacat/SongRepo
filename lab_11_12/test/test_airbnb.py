import pytest
from unittest import TestCase
from driver.driver_singleton import DriverSingleton
from page.main_page import MainPage
from page.residence_page import ResidencePage
from utils.loggers import TEST_LOGGER
from time import sleep
from utils.string_utils import is_english, is_czech
from configparser import ConfigParser


# pytest --html=resources/report/report.html test/test_airbnb.py


@pytest.mark.usefixtures("init_params")
class TestAirbnb(TestCase):
    def setUp(self):
        self.driver = DriverSingleton.get_driver(self.params['browser'])
        self.config = ConfigParser()
        self.config.read('config.ini')
        self.driver.maximize_window()
    

    def decorator_test(test):
        def wrapper(self, *args, **kwargs):
            try:
                TEST_LOGGER.debug(f'Run {test.__name__}')
                self.test_data = self.config[test.__name__]
                test(self, *args, **kwargs)
            except:
                self.driver.save_screenshot(f'resources/screenshots/{test.__name__}.png')
                raise
        return wrapper


    @decorator_test
    def test_main_page_currency_covertation(self):
        '''Test case 1'''
        page = MainPage(self.driver)
        page.open(self.test_data['link'])
        start_price = page.get_first_residence_price()
        sleep(3)
        page.set_currency_PLN()
        final_price = page.get_first_residence_price()
        self.assertTrue(start_price != final_price)


    @decorator_test
    def test_booking_price_convertation(self):
        '''Test case 2'''
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


    @decorator_test
    def test_region_search(self):
        '''Test case 3'''
        region = self.test_data['region']
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.search_by_region(region)
        self.assertTrue(region in self.driver.current_url)


    @decorator_test
    def test_automatic_translation(self):
        '''Test case 4'''
        page = ResidencePage(self.driver)
        page.open(self.test_data['link'])
        page.switch_auto_translation()
        header = page.get_header()
        self.assertTrue(is_english(header))


    @decorator_test
    def test_automatic_translation_language_change(self):
        '''Test case 5'''
        page = ResidencePage(self.driver)
        page.open(self.test_data['link'])
        page.close_auto_translation_popup()
        sleep(3)
        page.set_region_сzech()
        header = page.get_header()
        self.assertTrue(is_czech(header))

    
    @decorator_test
    def test_category_save_after_region_change(self):
        '''Test case 8'''
        page = MainPage(self.driver)
        page.open_without_popup_check(self.test_data['link'])
        page.set_region_eesti()
        current_url = str(self.driver.current_url)
        self.assertTrue(self.test_data['tag'] in current_url)


    @decorator_test
    def test_filter_save_after_category_change(self):
        '''Test case 9'''
        page = MainPage(self.driver)
        page.open(self.test_data['link'])
        page.set_next_category()
        current_url = str(self.driver.current_url)
        self.assertTrue(self.test_data['tag'] in current_url)


    @decorator_test
    def test_residence_from_map(self):
        '''Test case 10'''
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.show_map()
        main_page.click_first_map_residence()
        first_map_residence_link = main_page.get_first_map_residence_link().partition('?')[0]
        main_page.open_first_map_residence_page()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url_value = str(self.driver.current_url).partition('?')[0]
        self.assertTrue(first_map_residence_link == current_url_value)
    

    def tearDown(self):
        DriverSingleton.close_driver()