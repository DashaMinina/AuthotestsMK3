import time

from appium.webdriver.common.appiumby import AppiumBy

from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage


def test_storage_entity_picking():
    driver = initialize_appium_driver()
    driver.implicitly_wait(50)

    base_page = BasePage(driver)

    base_page.authorization_start()
    time.sleep(5)
    base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
    base_page.authorization_MK('1', '1')
    time.sleep(6)
    base_page.select_task_queue('Отбор', 'Отбор МХ (базовые настройки)')
    assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/position1_value").text == '1-1-2-4'
    assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/position_value").text == 'EUR-000000338'
    base_page.type_value('EUR-000000338')
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-2'
    base_page.type_value('DOC2')
    base_page.assert_finish_sku_picking()
    time.sleep(2)