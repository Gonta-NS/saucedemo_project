from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    finish_button = '//*[@id="finish"]'

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.finish_button)))

    def click_finish_button(self):
        self.get_finish_button().click()

    def finish_order(self):
        self.get_current_url()
        self.click_finish_button()
        print("Оформление заказа")