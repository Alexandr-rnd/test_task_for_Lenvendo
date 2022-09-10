import os

import allure
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver_path", default="C:\drivers")
    parser.addoption("--url", default="qa.digift.ru/", )


def kreds():
    with open('kreds.txt', 'r') as autorisation:
        kreds = autorisation.readline()
        return kreds


@pytest.fixture
def base_url(request):
    base_url = request.config.getoption(f"--url")
    return f'http://{kreds()}@' + base_url


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver_path = request.config.getoption("--driver_path")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=f"{driver_path}\chromedriver")
    else:
        raise ValueError("don't find this driver..")

    @allure.step("Закрытие браузера...")
    def fin():
        driver.quit()

    request.addfinalizer(fin)
    driver.maximize_window()
    return driver
