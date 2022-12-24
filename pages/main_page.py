from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    select_product_1 = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2 = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3 = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//*[@id="shopping_cart_container"]/a'
    menu = '//*[@id="react-burger-menu-btn"]'
    about = '//*[@id="about_sidebar_link"]'

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_product_2)))
    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_product_3)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart)))
    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.menu)))
    def get_about(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.about)))

    def click_select_product_1(self):
        self.get_select_product_1().click()
    def click_select_product_2(self):
        self.get_select_product_2().click()
    def click_select_product_3(self):
        self.get_select_product_3().click()
    def click_cart(self):
        self.get_cart().click()
    def click_menu(self):
        self.get_menu().click()
    def click_about(self):
        self.get_about().click()

    def buy_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
        print("Продукт_1 добавлен в корзину")
    def buy_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
        print("Продукт_2 добавлен в корзину")
    def buy_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()
        print("Продукт_3 добавлен в корзину")

