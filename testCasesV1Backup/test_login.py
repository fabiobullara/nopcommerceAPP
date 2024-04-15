import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage  # This is the class we created

class Test_001_Login:  # Test case ID
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):  # this makes use of the conftest.py for re-usability
        self.driver = setup  # this makes use of the conftest.py for re-usability
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":  # Right-click page, Inspect > Head > Title
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):  # this was used more than once, so it's moved to conftest.py
        self.driver = setup  # this was used more than once, so it's moved to conftest.py
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)  # lp is our object instance name, creating it invokes
        self.lp.setUserName(self.username)  # __init__(), which expects the driver parameter.
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title  # Capture the page title in act_title variable

        if act_title == "Dashboard / nopCommerce administration":  # Right-click page, Inspect > Head > Title
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
