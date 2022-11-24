from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class PasteCreationPage:
    def __init__(self, driver):
        self.driver = driver
        self.title_locator = (By.ID, 'postform-name')
        self.text_locator = (By.ID, 'postform-text')
        self.expiration_dropdown_locator = (By.ID, 'select2-postform-expiration-container')
        self.highlight_dropdown_locator = (By.ID, 'select2-postform-format-container')
        self.create_button_locator = (By.XPATH, "//button[text()='Create New Paste']")
    
    def open(self):
        self.driver.get('https://pastebin.com')

    def set_title(self, title: str):
        title_field = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.title_locator))
        title_field.send_keys(title)

    def set_text(self, text: str):
        text_area = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.text_locator))
        text_area.send_keys(text)

    def set_bash_highlight(self):
        highlight_dropdown = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.highlight_dropdown_locator))
        highlight_dropdown.click()
        highlight_element = self.driver \
            .find_element(By.XPATH, "(//ul[@id='select2-postform-format-results']//li[text()='Bash'])[1]")
        highlight_element.click()

    def set_expiration_time_10_minutes(self):
        expiration_dropdown = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.expiration_dropdown_locator))
        expiration_dropdown.click()
        expiration_time_element = self.driver \
            .find_element(By.XPATH, "//ul[@id='select2-postform-expiration-results']/li[text()='10 Minutes']")
        expiration_time_element.click()

    def create_paste(self):
        create_button = WebDriverWait(self.driver, 30) \
            .until(EC.presence_of_element_located(self.create_button_locator))
        create_button.click()