from datetime import datetime

import allure

import pytest

from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selene import browser, support
from selenium.common import InvalidSessionIdException


@pytest.fixture(scope='function', autouse=True)
def mobile_management():

    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'platformVersion': '10.0',
        'deviceName': 'fed896df0506',
        'appPackage': 'ru.axelot.mobileupdater',
        'appActivity': 'ru.axelot.mobileupdater.presentation.activity.LoginActivity',
        # 'appPackage': 'ru.axelot.wmsx5',
        # 'appActivity': 'ru.axelot.wmsx5',
        "noReset": True,  # Сохраняет кэш и данные приложения
        "fullReset": False,
        'app': "C:\\Users\\dasha\\PycharmProjects\\AuthotestsMK3\\apk\\Launcher_1.0.1.0-release.apk",
        # 'app': "C:\\Users\\dasha\\PycharmProjects\\AuthotestsMK3\\apk\\WMS_X5_5.0.9.6 prod 0.2-release.apk",
        'waitForIdleTimeout': 10
    })
    driver = webdriver.Remote('http://192.168.0.104:4723', options=options)
    # return driver

    yield driver

    try:
        driver.quit()
    except InvalidSessionIdException:
        pass
    # browser.config.driver_remote_url = 'http://192.168.0.107:4723'
    # browser.config.driver_options = options

# def make_screenshot():
#     driver = mobile_management
#     allure.attach(
#
#         driver.get_screenshot_as_png(),
#         name="Скриншот ошибки",
#         attachment_type=allure.attachment_type.PNG
#     )

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Make screenshot"""
#     outcome = yield
#     result = outcome.get_result()
#     if item.when == "call" and result.failed is True:
#         make_screenshot()









