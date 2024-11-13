import time

from appium.webdriver.common.appiumby import AppiumBy

from config.appium_utils import initialize_appium_driver


def test_placement():

    driver = initialize_appium_driver()
    driver.implicitly_wait(50)

    driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/connect_button").click()
    time.sleep(6)
    start_x = 200
    start_y = 600
    end_x = 200
    end_y = 100
    duration = 400  # Время анимации свайпа в миллисекундах
    driver.swipe(start_x, start_y, end_x, end_y, duration)
    driver.swipe(start_x, start_y, end_x, end_y, duration)
    driver.swipe(start_x, start_y, end_x, end_y, duration)
    driver.swipe(start_x, start_y, end_x, end_y, duration)
    driver.swipe(start_x, start_y, end_x, end_y, duration)

    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='WMSBaseTestDI']").click()
    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='WMSBaseTestDI']").click()

    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/login_input").send_keys('1')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/password_input").send_keys('1')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/connect_button").click()
    time.sleep(6)
    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Размещение']").click()
    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Размещение МХ (базовые настройки)']").click()
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('EUR-000000314')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'B-2-1'
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('B21')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000315'
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('EUR-000000315')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'B-2-2'
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('B22')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)




