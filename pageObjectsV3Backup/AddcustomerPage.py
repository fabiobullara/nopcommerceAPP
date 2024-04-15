import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]" # use descriptive variable names
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"

    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"               # manually generated xpath
    # The above 'Customer Roles' field is actually considered a textbox (not a dropdown)
    # Below are the 4 roles (or options) of the above text box
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"                 # manually generated xpath
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"                         # manually generated xpath
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"                                 # manually generated xpath
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"                               # manually generated xpath

    drpmrgOfVendor_xpath = "//*[@id='VendorId']"   # This is a dropdown (you can tell by the 'select' on inspection)
    rdMaleGender_id = "Gender_Male"                                                         # using id instead of xpath
    rdFemaleGender_id = "Gender_Female"                                                     # using id instead of xpath
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
#    ckbIsTaxExempt_xpath = "//input[@id='IsTaxExempt']"         # intentionally left out in video
#    ckbActive_xpath = "//input[@id='Active']"                   # intentionally left out in video
    btnSave_xpath = "//button[@name='save']"

    # We first need to create a constructor

    def __init__(self, driver):     # Gets driver from test case and initiates the local driver
        self.driver = driver        # Because the driver now belongs to the class, we access it using 'self'

    # For every element above, we need to create an action method

    def clickOnCustomersMenu(self):     # User defined names (should be descriptive and consistent)
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):     # User defined names (should be descriptive and consistent)
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):     # User defined names (should be descriptive and consistent)
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):     # User defined names (should be descriptive and consistent)
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)         # email comes from the test case

    def setPassword(self, password):     # User defined names (should be descriptive and consistent)
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)   # password comes from the test case

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):  # only one can be set, gender comes from the test case
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Site restriction: here user can be either Registered or Guest, but only one
            time.sleep(3)
            # The line below removes 'Registered', as you cannot submit Guests and Registered in the form
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
            time.sleep(3)
            # self.listitem.click();  # This doesn't work, so we execute the JavaScript below
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
