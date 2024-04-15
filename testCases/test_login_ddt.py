import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage         # This is the class we created
from utilities.readProperties import ReadConfig     # to directly access (static) methods from readProperties.py
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:  # Test case ID

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()            # we call it directly from the LogGen class because it's a static method

    @pytest.mark.regression                 # test grouping marker
    # test grouping marker
    def test_login_ddt(self, setup):    # this was used more than once, so it's moved to conftest.py
        self.logger.info("*************** Test_002_DDT_Login ***************")
        self.logger.info("******** Verifying Login DDT Test - start ********")
        self.driver = setup             # this was used more than once, so it's moved to conftest.py
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)  # lp is our LoginPage object instance name, creating it invokes __init__.py

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in Excel: ", self.rows)

        lst_status = []     # Empty list variable to be used later

        for r in range(2, self.rows+1):     # this loop is repeated for the number of rows (r) in the data file
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)         # reads the first column of the given row
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)     # reads the second column of the given row
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)          # reads the third column of the given row

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            print("row: " + str(r), ", username: " + self.user, ", password: " + self.password, ", exp: " + self.exp)

            # Validation:
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************ Login successful and expecting pass, TC Passed ***********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("************ Login successful but expecting fail, TC Failed ***********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("************ Login unsuccessful & expecting pass, TC Failed ***********")
#                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("************ Login unsuccessful & expecting fail, TC Passed ***********")
#                    self.lp.clickLogout()
                    lst_status.append("Pass")
            if "Fail" not in lst_status:        # This determines if the overall test case passed or failed
                self.logger.info("***** Login DDT test cases passed *****")    # Final status
                assert True
            else:
                self.logger.info("***** Login DDT test cases failed *****")
                assert False

        self.driver.close()

        self.logger.info("*************** End of Test_002_DDT_Login Test ***************")
        self.logger.info("***************** Login DDT Test - completed *****************")
