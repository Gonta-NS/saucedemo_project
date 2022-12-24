from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locator_first_name = '//*[@id="first-name"]'
    locator_last_name = '//*[@id="last-name"]'
    locator_postal_code = '//*[@id="postal-code"]'
    locator_button_continue = '//*[@id="continue"]'

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_last_name)))
    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_postal_code)))
    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.locator_button_continue)))

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
    def click_button_continue(self):
        self.get_button_continue().click()

    def input_info(self):
        self.get_current_url()
        self.input_first_name('Nazar')
        self.input_last_name('Gonta')
        self.input_postal_code('141070')
        self.click_button_continue()
        print("Данные покупателя заполнены")