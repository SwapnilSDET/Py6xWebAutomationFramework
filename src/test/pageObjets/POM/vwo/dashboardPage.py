# Dashboard Page Class

"""
1. Create a class
2. Create a constructor
3. Create page locators as a tuple
4. Define the page locators using get method
5. Define the page actions
"""


from selenium.webdriver.common.by import By
from src.test.utils.commom_utils import webdriver_wait


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    ## Page Locators - Need to set as a Tuple
    user_logged_in = (By.XPATH, "//div[@data-qa='nadoqazuxo']/selected-value-slot/span[1]")
    user_logged_in_user_ID = (By.XPATH, "//div[@data-qa='nadoqazuxo']/selected-value-slot/span[2]")

    ## Setting up the locators using Getters
    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def logged_in_username_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.user_logged_in, timeout=15)
        return self.get_user_logged_in().text