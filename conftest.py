from selenium import webdriver
from selenium.webdriver import Chrome
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()


@pytest.fixture(scope='class')

def setup(request): # It takes request

    driver.maximize_window()

    username = os.getenv("VALID_USERNAME")
    password = os.getenv("VALID_PASSWORD")
    logged_in_username = os.getenv("LOGGED_IN_USERNAME")

    invalid_username = os.getenv("INVALID_USERNAME")
    invalid_password = os.getenv("INVALID_PASSWORD")
    invalid_msg_error = os.getenv("error_message_expected")


    # -------------------------

    request.cls.driver = driver

    request.cls.username = username
    request.cls.password = password
    request.cls.logged_in_username = logged_in_username

    request.cls.invalid_username = invalid_username
    request.cls.invalid_password = invalid_password
    request.cls.invalid_msg_error = invalid_msg_error


    yield driver  # return driver - tear-down method
    driver.quit()