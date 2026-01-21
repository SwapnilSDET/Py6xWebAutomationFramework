import time

from seleniumpagefactory.Pagefactory import PageFactory
from src.test.utils.commom_utils import *
from src.test.utils.commom_utils import webdriver_wait

class DashboardPage(PageFactory):
    # Webdriver - Init
    def __init__(self, driver):
        self.driver = driver
        self.highlight = True

    locators = {
        'username_logged_in': ('XPATH', "//div[@data-qa='nadoqazuxo']/selected-value-slot/span[1]")
    }

    def user_logged_in_text(self):
        webdriver_wait_url(driver=self.driver, timeout=10)
        return self.username_logged_in.get_text()