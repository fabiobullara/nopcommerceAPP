from selenium.webdriver.common.by import By


class LoginPage:                                                    # Page Object Class

    # Page Object Locators:
    textbox_username_id = "Email"                                 # text field
    textbox_password_id = "Password"                              # text field
    button_login_xpath = "//button[contains(text(),'Log in')]"    # button (no avail id)
    link_logout_linktext = "Logout"                               # text link

    # Python Constructor - Invoked at object creation

    def __init__(self, driver):     # Driver will come from Test Case.
        self.driver = driver

        # Captures driver from test cases and passes it to class variable
        # and will be used to drive all action methods for these elements.

        # Action Methods for each Locator (they will be called from the test cases)

    def setUserName(self, username):    # username will come from the test case
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

# Method names can be anything, but should be unique.
