import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver

# @pytest.fixture(scope='function', autouse=True)
def initialize_appium_driver():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'platformVersion': '10.0',
        'deviceName': 'fed896df0506',
        'appPackage': 'ru.axelot.mobileupdater',
        'appActivity': 'ru.axelot.mobileupdater.presentation.activity.LoginActivity',
        "noReset": True,  # Сохраняет кэш и данные приложения
        "fullReset": False,
        'app': "C:\\Users\\dasha\\PycharmProjects\\AuthotestsMK3\\apk\\Launcher_1.0.0.12-release.apk",
        'waitForIdleTimeout': 0
        })
    driver = webdriver.Remote('http://192.168.0.107:4723', options=options)
    return driver

