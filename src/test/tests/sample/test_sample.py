import allure
import pytest
import time


@allure.title("Dry-run for the passed test case")
@allure.description("TC#1 - Dry-run for the passed test case")
def test_sample_pass():
    print("test_sample_pass")
    assert True == True

@allure.title("Dry-run for the failed test case")
@allure.description("TC#2 - Dry-run for the failed test case")
def test_sample_fail():
    print("test_sample_fail")
    assert True == False