import allure
import pytest
import time


@allure.title("Dry Run of the Passed Testcase")
@allure.description("TC#1Dry Run of the Passed Testcase")
def test_sample_pass():
    print("Hi")
    assert True == True


@allure.title("Dry Run of the Failed Testcase")
@allure.description("TC#2 Dry Run of the Failed Testcase")
def test_sample_fail():
    print("Hi")
    assert True == False
