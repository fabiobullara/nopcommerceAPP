import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random


class Test_003_AddCustomer:  # Test case ID

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    # Logger

    def test_addCustomer(self, setup):          # setup is defined in conftest.py

        self.logger.info("************** Test_003_AddCustomer **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # The Login methods being called below are defined in the LoginPage.py file
        self.lp = LoginPage(self.driver)        # self.lp is the page object from the LoginPage class

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************** Login Successful **************")

        self.logger.info("********* Starting Add Customer Test *********")
        self.addcust = AddCustomer(self.driver)         # object of AddCustomer class in the page object
        time.sleep(3)
        self.addcust.clickOnCustomersMenu()
        time.sleep(3)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(3)
        self.addcust.clickOnAddnew()

        self.logger.info("********** Providing Customer Info ***********")
        self.email = random_generator() + "@gmail.com"   # generates unique email, see random_generator() below
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/1985")    # Format: DD/MM/YYYY
        self.addcust.setCompanyName("busyQA")
        # self.addcust.setCustomerRoles("Guests")
        # self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing .......")
        time.sleep(3)
        self.addcust.clickOnSave()
        self.logger.info("************ Saving Customer Info ***********")

        self.logger.info("********** Add Customer Validation **********")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text    # Captures all text in the confirmation page
        print("self.msg: ", self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")    # Capture screenshot
            self.logger.error("********** Add Customer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("**** Test_003_AddCustomer Test Completed ****")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
