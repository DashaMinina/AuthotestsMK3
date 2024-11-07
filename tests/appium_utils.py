import pytest

from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver

# @pytest.fixture(scope='function')
def initialize_appium_driver():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'platformVersion': '10.0',
        'deviceName': 'fed896df0506',
        'appPackage': 'ru.axelot.mobileupdater',
        'appActivity': 'ru.axelot.mobileupdater.presentation.activity.LoginActivity',
        "noReset": True,  # Сохраняет кэш и данные приложения
        "fullReset": False,
        # 'app': "C:\\Users\\dasha\\PycharmProjects\\AuthotestsMK3\\apk\\Launcher_1.0.0.12-release.apk",
        'waitForIdleTimeout': 0,
        # 'optionalIntentArguments': f"--es axelot_launch_data {'serverAddress':'192.168.0.78','additionalData':{'restoreConnection':'true', 'port': '13200'}}",
        # "ignoreUnimportantViews": True,
        # "disableAndroidWatchers": True,
    })
    # options.optional_intent_arguments = options.optional_intent_arguments = '--es %s "%s"' % (
    #     "axelot_launch_data", {"serverAddress":"192.168.101.9","additionalData":{"restoreConnection":"true", "port": "5275"}})
    driver = webdriver.Remote('http://192.168.0.107:4723', options=options)

    # browser.config.driver_remote_url = 'http://192.168.0.107:4723'
    # browser.config.driver_options = options
    return  driver
    # yield driver
    # driver.quit()