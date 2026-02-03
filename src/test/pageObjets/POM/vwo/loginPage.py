from selenium.webdriver.common.by import By
from src.test.utils.commom_utils import webdriver_wait


"""
1. Create a class
2. Create a constructor
3. Create page locators as a tuple
4. Define the page locators using get method
5. Define the page actions
"""

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    ## Page Locators - Need to set as a Tuple
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")
    free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")
    # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")


    ## Setting up the locators
    def get_username(self):
        return self.driver.find_element(*LoginPage.username) # *ClassName.LocatorVarName

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_free_trial_button(self):
        return self.driver.find_element(*LoginPage.free_trail)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    ## Page Actions

    # To perform login action
    def login_to_vwo(self, usr, pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()
        except Exception as e:
            print(e)

    # To fetch an error message in case of login via invalid creds are attempted.
    def get_error_message_as_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.error_message, timeout=5)
        return self.get_error_message().text

    # To perform click action on the "Start a free trial" link
    def free_trial_button_click(self):
        try:
            self.get_free_trial_button().click()
        except Exception as e:
            print(e)
