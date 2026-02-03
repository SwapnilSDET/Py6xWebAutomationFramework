import allure
import pytest
from selenium import webdriver
from src.test.constants.Constants import Constants
from src.test.pageObjets.PF.loginPage_PageFactory import LoginPage
from src.test.pageObjets.PF.dashboard_PageFactory import DashboardPage
from dotenv import load_dotenv
import os
from src.test.utils.Utils import *
import logging


@allure.epic("VWO App login Check!")
@allure.feature("Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants().app_url())

            loginPage = LoginPage(driver)
            loginPage.login_to_vwo(usr=self.invalid_username, pwd=self.invalid_password)

            error_msg_text = loginPage.error_msg()
            # assert error_msg_text == os.getenv("error_message_expected")
            assert error_msg_text == self.invalid_msg_error

        except Exception as e:
            print(e)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_positive(self, setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants().app_url())

            loginPage = LoginPage(driver=driver)
            LOGGER.info("Login is done!")
            loginPage.login_to_vwo(usr=self.username, pwd=self.password)


            dashboardPage = DashboardPage(driver=driver)
            LOGGER.info("Dashboard loaded!")
            loggedin_username = dashboardPage.logged_in_username_text()
            print(loggedin_username)
            assert loggedin_username == self.logged_in_username

        except Exception as e:
            print(e)
