from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

standard_user = 'standard_user'
locked_out_user = 'locked_out_user'
problem_user = 'problem_user'
performance_glitch_user = 'performance_glitch_user'
password_all = 'secret_sauce'

class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    user_name = '//*[@id="user-name"]'
    password = '//*[@id="password"]'
    login = '//*[@id="login-button"]'
    mait_word = '//*[@id="header_container"]/div[2]/span'

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.password)))
    def get_login(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login)))
    def get_mait_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.mait_word)))

    def input_user_name(self, name):
        self.get_user_name().send_keys(name)
    def input_password(self, passwrd):
        self.get_password().send_keys(passwrd)
    def click_login(self):
        self.get_login().click()

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_user_name(standard_user)
        self.input_password(password_all)
        self.click_login()
        print("Залогинились")