from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class PastePage:
    def __init__(self, driver):
        self.driver = driver
        self.title_locator = (By.XPATH, "//div[@class='info-top']/h1")
        self.highlight_locator = (By.XPATH, "//a[starts-with(@href, '/archive/')]")

    def get_title(self) -> str:
        return WebDriverWait(self.driver, 15) \
            .until(EC.presence_of_element_located(self.title_locator)).text

    def get_highlight(self) -> str:
        return WebDriverWait(self.driver, 15) \
            .until(EC.presence_of_element_located(self.highlight_locator)).text

    def get_text(self) -> str:
        raw_link = self.driver.find_element(By.XPATH, "//a[text()='raw']")
        raw_link.click()
        text = WebDriverWait(self.driver, 15) \
            .until(EC.presence_of_element_located((By.TAG_NAME, "pre"))).text
        self.driver.back()
        return text