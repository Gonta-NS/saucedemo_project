from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    checkout = '//*[@id="checkout"]'

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkout)))

    def click_checkout(self):
        self.get_checkout().click()

    def get_checkout_button(self):
        self.get_current_url()
        self.click_checkout()
        print('Товар добавлен в корзину')
