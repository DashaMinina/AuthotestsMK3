import time

from appium.webdriver.common.appiumby import AppiumBy

from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage


def test_sku_picking():
    driver = initialize_appium_driver()
    driver.implicitly_wait(50)

    base_page = BasePage(driver)

    base_page.authorization_start()
    time.sleep(5)
    base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
    base_page.authorization_MK('1', '1')
    time.sleep(6)
    base_page.select_task_queue('Отбор', 'Отбор ОХ (базовые настройки)')
    assert driver.find_element(AppiumBy.ID,
                               "ru.axelot.wmsx5:id/textViewTip").text == 'Введите место хранения для отбора Заказ на отгрузку № 00000000001 от 25.09.2024'
    base_page.type_value('EUR-000000332')
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == '2-4-2-1'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location2_value").text == 'EUR-000000331'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '25092024'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 70 Флакон'
    base_page.type_value('EUR-000000331')
    base_page.type_value('2704065335623')
    base_page.type_value('70')
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == '1-1-3-1'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location2_value").text == 'EUR-000000330'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Наушники'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 55 шт'
    base_page.type_value('EUR-000000330')
    base_page.type_value('2620424001643')
    base_page.type_value('55')
    time.sleep(1)
    base_page.type_value('DOC2')
    base_page.assert_finish_sku_picking()
    time.sleep(2)