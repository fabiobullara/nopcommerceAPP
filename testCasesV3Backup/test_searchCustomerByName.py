import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig     # to directly access (static) methods from readProperties.py
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByName(self, setup):
        self.logger.info("****************** SearchCustomerByName_005 ******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # We start by logging in, leveraging the existing LoginPage object class
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Loging Successful ******************")

        self.logger.info("********** Starting Search Customer By Name **********")

        # We navigate to the search page, leveraging the existing AddcustomerPage object class
        self.addcust = AddCustomer(self.driver)
        time.sleep(3)
        self.addcust.clickOnCustomersMenu()
        time.sleep(3)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(3)

        self.logger.info("********** Searching Customer by Name **********")

        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")

        assert True == status       # if 'status' == 'True', the assertion passes, otherwise it fails
        self.logger.info("********** TC_SearchCustomerByName_005 Completed **********")
        self.driver.close();