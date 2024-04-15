import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage         # This is the class we created
from utilities.readProperties import ReadConfig     # to directly access (static) methods from readProperties.py
from utilities.customLogger import LogGen


class Test_001_Login:  # Test case ID

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()        # we call it directly from the LogGen class because it's a static method

    @pytest.mark.regression             # test grouping marker
    def test_homePageTitle(self, setup):        # this makes use of conftest.py for re-usability

        self.logger.info("********** test_homePageTitle() Test Case **********")
        self.logger.info("********** Verifying Home Page Title test - start **********")
        self.driver = setup                     # this makes use of conftest.py for re-usability
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":    # Right-click page, Inspect > Head > Title
            self.driver.close()
            self.logger.info("********** Home page title test passed **********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home page title test failed **********")
            assert False

    @pytest.mark.sanity                 # test grouping marker
    @pytest.mark.regression             # test grouping marker
    def test_login(self, setup):  # this was used more than once, so it's moved to conftest.py

        self.logger.info("********** test_login() Test Case **********")
        self.logger.info("********** Verifying Login Test - start **********")
        self.driver = setup  # this was used more than once, so it's moved to conftest.py
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)  # lp is our object instance name, creating it invokes
        self.lp.setUserName(self.username)  # __init__(), which expects the driver parameter.
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title  # Capture the page title in act_title variable

        if act_title == "Dashboard / nopCommerce administration":  # Right-click page, Inspect > Head > Title
            self.driver.close()
            self.logger.info("********** Login test passed **********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********** Login test failed **********")
            assert False
