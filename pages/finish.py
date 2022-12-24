from base.base_class import Base

class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def finishing(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()
        print("Скриншот сделан")