from selenium import webdriver
import logging


logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.CRITICAL)
logging.getLogger('selenium.webdriver.common.service').setLevel(logging.CRITICAL)
logging.getLogger('urllib3.connectionpool').setLevel(logging.CRITICAL)


class DriverSingleton:
    _driver = None


    @classmethod
    def get_driver(cls, browser: str):
        if cls._driver is not None:
            return cls._driver
        
        match browser:
            case 'firefox':
                cls._driver = webdriver.Firefox()
            case 'edge':
                cls._driver = webdriver.Edge()
        return cls._driver
    

    @classmethod
    def close_driver(cls):
        cls._driver.quit()
        cls._driver = None
