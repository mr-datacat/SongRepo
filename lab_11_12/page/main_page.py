from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumpagefactory.Pagefactory import PageFactory
from page.residence_page import ResidencePage
from time import sleep
from utils.loggers import PAGE_LOGGER
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.map_locators = {
            'first_map_residence': (By.XPATH, "(//button[@data-veloute='map/markers/BasePillMarker'])[1]"),
            'first_map_residence_block': (By.XPATH, "(//div[contains(@aria-labelledby, 'title')])[1]"),
            'first_map_residence_link': (By.XPATH, "(//a[contains(@aria-labelledby, 'title')])[1]")
        }
        self.search_locators = {
            'search_field': (By.ID, 'bigsearch-query-location-input'),
            'search_commit_button': (By.XPATH, "//button[@data-testid='structured-search-input-search-button']"),
            'first_found_residence': (
                By.XPATH, 
                "(//img[@id='FMP-target'])[1]"
            )
        }
        self.language_locators = {
            'EE': (By.XPATH, "//a[@lang='et-EE']")
        }
        self.currency_locators = {
            'PLN': (By.XPATH, "//div[text()='PLN – zł']")
        }

    
    locators = {
        'first_residence': ('XPATH', "(//div/a[@tabindex='-1'])[1]"),
        'first_residence_price': (
            'XPATH',
            "/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div/div/span/div/span[1]"
        ),
        'region_search': ('XPATH', "//button[@data-index='0']"),
        'region_settings': ('XPATH', "//button[@aria-label='Choose a language and currency']"),
        'currency_settings': ('XPATH', "//button//span[text()='USD']"),
        'next_category': (
            'XPATH', 
            "(//div[@data-plugin-in-point-id='CATEGORY_FILTER_BAR']//button[@role='radio'])[2]"
        ),
        'map': ('XPATH', "//span[text()='Show map']")
    }

    
    def open(self, link: str=None):
        self.open_without_popup_check(link)
        self.close_popup()
        sleep(1)
    

    def open_without_popup_check(self, link: str=None):
        PAGE_LOGGER.info('Open main page')
        if link is None:
            self.driver.get('https://www.airbnb.ru/?locale=en&enable_auto_translate=false')
        else:
            self.driver.get(link)
        sleep(4)
    
    
    def close_popup(self):
        close_popup_button = WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']")))
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(
            to_element=close_popup_button, 
            xoffset=-80, 
            yoffset=0
            )
        action.click()
        action.perform()
        sleep(2)
    

    def open_first_residence(self) -> ResidencePage:
        PAGE_LOGGER.info('Open first residence page')
        self.first_residence.click()
        sleep(4)
        return ResidencePage(self.driver)
    
    
    def show_map(self):
        PAGE_LOGGER.info('Open map')
        self.map.click()

    
    def click_first_map_residence(self):
        PAGE_LOGGER.debug('Click first map residence')
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.map_locators['first_map_residence'])).click()

    
    def get_first_map_residence_link(self) -> str:
        PAGE_LOGGER.debug('Get first map residence link')
        link = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.map_locators['first_map_residence_link']))
        return link.get_attribute("href")
    
    
    def open_first_map_residence_page(self) -> ResidencePage:
        PAGE_LOGGER.info('Open first map residence page')
        WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.map_locators['first_map_residence_block'])).click()
        return ResidencePage(self.driver)


    def search_by_region(self, region: str):
        PAGE_LOGGER.info(f"Search by region '{region}'")
        self.region_search.click()
        
        PAGE_LOGGER.debug('Send keys')
        search_field = WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.search_locators['search_field']))
        search_field.send_keys(region)
        search_field.send_keys(Keys.ENTER)
        
        PAGE_LOGGER.debug('Commit search')
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.search_locators['search_commit_button'])) \
            .click()
    

    def open_first_region_searched_residence(self) -> ResidencePage:
        PAGE_LOGGER.info("Open first found page")
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.search_locators['first_found_residence'])) \
            .click()
        sleep(2)
        return ResidencePage(self.driver)
    

    def set_region_eesti(self):
        PAGE_LOGGER.info("Set region Eesti")
        self.region_settings.click()
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.language_locators['EE'])) \
            .click()
        sleep(2)
    

    def set_next_category(self):
        PAGE_LOGGER.info("Set next category")
        self.next_category.click()
        sleep(2)
    

    def set_currency_PLN(self):
        PAGE_LOGGER.info("Set currency PLN")
        self.currency_settings.click()
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable(self.currency_locators['PLN'])) \
            .click()
        sleep(4)
    

    def get_first_residence_price(self):
        PAGE_LOGGER.debug('Get first residence price')
        price = self.first_residence_price.text
        return price
