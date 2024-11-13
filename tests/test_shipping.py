import time
from appium.webdriver.common.appiumby import AppiumBy
from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage



def test_shipping():
    driver = initialize_appium_driver()
    driver.implicitly_wait(50)

    base_page = BasePage(driver)

    base_page.authorization_start()
    time.sleep(5)
    base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
    base_page.authorization_MK('1', '1')
    time.sleep(6)
    base_page.select_task_queue('Отгрузка', 'Отгрузка')
    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/document_title' and @text='Заказ на отгрузку 00000000004 от 25.09.2024']").click()
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-2'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000350'
    base_page.type_value('EUR-000000350')
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "android:id/alertTitle").text == 'Подтверждение выполнения'
    assert driver.find_element(AppiumBy.ID, "android:id/message").text == 'Грузовое место EUR-000000350 отгружено?'
    driver.find_element(AppiumBy.ID, "android:id/button1").click()
    base_page.assert_finish_shipping()
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-2'
    # base_page.type_value('DOC2')
    # base_page.assert_finish_sku_picking()
    # time.sleep(2)