# Assertions and use the Page Object class
import pytest
# Webdriver Start
# User Interaction + Assertions
# Close Webdriver


from selenium import webdriver
from src.test.constants.Constants import Constants
from src.test.utils.Utils import *

from src.test.pageObjets.POM.vwo.loginPage import LoginPage
from src.test.pageObjets.POM.vwo.dashboardPage import DashboardPage

from dotenv import load_dotenv
import os



@pytest.fixture
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get(Constants.app_url()) - In case of Static
    driver.get(Constants().app_url()) # - In case of Non-static
    return driver


@allure.title("VWO Login Test")
@allure.id("JIRA_ID_1234")
@allure.description("TC#0 - VWO App Negative Test")
@allure.feature("Feature | VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup

    login_page = LoginPage(driver)
    login_page.login_to_vwo(
        usr=os.getenv("INVALID_USERNAME"),
        pwd=os.getenv("INVALID_PASSWORD")
    )
    error_msg_element_text = login_page.get_error_message_as_text()
    take_screen_shot(driver=driver, name="test_vwo_login_negative")
    assert error_msg_element_text == os.getenv("error_message_expected")


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup

    # LoginPage actions - Login with valid creds
    login_page = LoginPage(driver=driver)
    login_page.login_to_vwo(
        usr=os.getenv("VALID_USERNAME"),
        pwd=os.getenv("VALID_PASSWORD")
    )

    # DashboardPage actions - Access the username & vetrify the same
    dashboard_page = DashboardPage(driver=driver)
    user_name = dashboard_page.logged_in_username_text()
    take_screen_shot(driver=driver, name="test_vwo_login_positive")
    assert os.getenv("LOGGED_IN_USERNAME") == user_name