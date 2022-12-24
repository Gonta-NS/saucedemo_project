import pytest
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.info_page import Info_page
from pages.payment_page import Payment_page
from pages.finish import Finish_page

@pytest.mark.run(order=3)
def test_select_product_1():
    driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\browser_driver\\chromedriver.exe\\')
    login = Login_page(driver)
    login.authorization()
    main = Main_page(driver)
    main.buy_product_1()
    cart = Cart_page(driver)
    cart.click_checkout()
    info = Info_page(driver)
    info.input_info()
    payment = Payment_page(driver)
    payment.finish_order()
    finish = Finish_page(driver)
    finish.finishing()

@pytest.mark.run(order=2)
def test_select_product_2():
    driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\browser_driver\\chromedriver.exe\\')
    login = Login_page(driver)
    login.authorization()
    main = Main_page(driver)
    main.buy_product_2()
    cart = Cart_page(driver)
    cart.click_checkout()

@pytest.mark.run(order=1)
def test_select_product_3():
    driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\browser_driver\\chromedriver.exe\\')
    login = Login_page(driver)
    login.authorization()
    main = Main_page(driver)
    main.buy_product_3()
    cart = Cart_page(driver)
    cart.click_checkout()
