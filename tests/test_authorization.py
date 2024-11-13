import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, command

from config.appium_utils import initialize_appium_driver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction


def click_on_coordinates(driver, x, y, x1, y1):
    action = ActionChains(driver)
    action.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    action.w3c_actions.pointer_action.move_to_location(x, y)
    action.w3c_actions.pointer_action.pointer_down()
    # action.w3c_actions.pointer_action.pause(2)
    action.w3c_actions.pointer_action.move_to_location(x1, y1)
    action.w3c_actions.pointer_action.release()
    action.perform()

#потом обернуть авторизацию в фикстуру и перенести в confest

def test_authorization_MK():
    driver = initialize_appium_driver()
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/login_input").send_keys('1')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/password_input").send_keys('1')
    time.sleep(15)

def test_authorization_start():
        # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/login_edit")).type('admin')
        # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/password_edit")).type('admin')
        # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/address_edit")).type('192.168.101.9:5275')
        # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/connect_button")).click()
        # time.sleep(1)
        # browser.element((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']")).click()
    driver = initialize_appium_driver()
    driver.implicitly_wait(50)
        # driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/login_edit").send_keys('admin')
        # driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/password_edit").send_keys('admin')
        # driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/address_edit").send_keys('192.168.101.9:5275')
    driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/connect_button").click()
        # driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']").click()
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


    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']").click()
    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']").click()

        # driver.find_element(AppiumBy.ID, "android:id/button1").click()
        # driver.wait_activity(driver.find_element(AppiumBy.ID, "android:id/button1"))
        # time.sleep(200)
        # driver.wait_activity(driver.find_element(AppiumBy.ID, "android:id/button1").click())
        # time.sleep(60)
        # driver.wait_activity(driver.find_element(AppiumBy.ID, "com.miui.global.packageinstaller:id/btn_open_normal").click())
        # time.sleep(40)



    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/login_input").send_keys('1')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/password_input").send_keys('1')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/connect_button").click()
    time.sleep(6)
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Приемка']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Приемка (пересчет)']").click()
    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/document_title' and @text='Ожидаемое поступление 00000000015 от 11.10.2024']").click()
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('DOC1')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('EUR-000000364')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('2486095310145')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объектив 2.0'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '630'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 630 шт'
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('TR2_190429')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == 'TR2_190429'
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('2867549627970')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов 2.0'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '52000'
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 52000 Флакон'
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('11102024')
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '11102024'
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/floatingActionButton").click()
    time.sleep(2)
        # assert driver.find_element(AppiumBy.ID,
        #                                "ru.axelot.wmsx5:id/editText_bottom_panel").text == 'Завершить EUR-000000362'
    driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").click()
    time.sleep(2)
    assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Отсканируйте поддон'
    driver.back()
    assert driver.find_element(AppiumBy.ID, "android:id/message").text == 'Завершить приемку ожидаемого поступления? (все товары приняты)'
    driver.find_element(AppiumBy.ID, "android:id/button1").click()
    assert driver.find_element(AppiumBy.ID,
                               "ru.axelot.wmsx5:id/user_name").text == 'Привет, 1!'

    # for i in range(1,5) :
    #     try:
    #         driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']").click()
    #     except:
    #
    #         continue
    # driver.find_element(AppiumBy.XPATH,
    #                     "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']"). is
    # time.sleep(3)
    # driver.swipe(100,100, 100, 1000)
    # click_on_coordinates(driver, 100,500, 100, 800)
    # browser.all((AppiumBy.ID,"ru.axelot.mobileupdater:id/config_title")).element_by(have.exact_text("TG_WMS_X5_Release")).click()

    # browser.perform(command.js.scroll_into_view)
    # actions = ActionChains(browser.driver)
    # actions.scroll_by_amount(1000,2000)
    # actions.click(
    #     browser.element((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")))

    #time.sleep(10)
    # browser.with_(scroll_down_w3c()).element((AppiumBy.XPATH,"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")).click()
    # elems = browser.all((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title']"))

    #for i in elems:
    #    ...
        #print(i.get(query.text))
    # print(elems.get(query.text))
    time.sleep(5)
    #browser.element(AppiumBy.xpath("//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']")).click()

    #
    # browser.element(by.xpath("//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")).perform(command.js.scroll_into_view).click()
    # #print(elem_2)
    # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/project_title")).element(("WMS X5")).click()
    # browser.element(AppiumBy.ID, "ru.axelot.mobileupdater:id/config_title").
    # .should(have.text("WMS_FSlogistics_TST"))
    # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/project_title", texts("WMS X5"))).click()
    # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/config_title", texts("WMS_FSlogistics_TST"))).click()
    #time.sleep(60)

def test_receipt():
    # driver = initialize_appium_driver()
    # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/connect_button")).click()
    browser.element('#WMSBaseTestDI').perform(command.js.scroll_into_view)
    # element_by('#WMSBaseTestDI')
    # all('#config_title')
    # browser.element(AppiumBy.XPATH,
    #                     '//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='WMSBaseTestDI']').perform(command.js.scroll_into_view)
    #
    # time.sleep(6)
    # start_x = 200
    # start_y = 600
    # end_x = 200
    # end_y = 100
    # duration = 400  # Время анимации свайпа в миллисекундах
    # driver.swipe(start_x, start_y, end_x, end_y, duration)
    # driver.swipe(start_x, start_y, end_x, end_y, duration)
    # driver.swipe(start_x, start_y, end_x, end_y, duration)
    # driver.swipe(start_x, start_y, end_x, end_y, duration)
    #
    # driver.find_element(AppiumBy.XPATH,
    #                     "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']").click()
    # driver.find_element(AppiumBy.XPATH,
    #                     "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']").click()


    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/login_input").send_keys('1')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/password_input").send_keys('1')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/connect_button").click()
    # time.sleep(6)
    # driver.find_element(AppiumBy.XPATH,
    #                     "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Приемка']").click()
    # driver.find_element(AppiumBy.XPATH,
    #                     "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Приемка (пересчет)']").click()
    # driver.find_element(AppiumBy.XPATH,
    #                     "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/document_title' and @text='Ожидаемое поступление 00000000015 от 11.10.2024']").click()
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('DOC1')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # time.sleep(2)
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('EUR-000000364')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # time.sleep(2)
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('2486095310145')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # time.sleep(2)
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объектив 2.0'
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '630'
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 630 шт'
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('TR2_190429')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # time.sleep(2)
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == 'TR2_190429'
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # time.sleep(2)
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('2867549627970')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # time.sleep(2)
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов 2.0'
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '52000'
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 52000 Флакон'
    # time.sleep(2)
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('11102024')
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # time.sleep(2)
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '11102024'
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/floatingActionButton").click()
    # time.sleep(2)
    # # assert driver.find_element(AppiumBy.ID,
    # #                                "ru.axelot.wmsx5:id/editText_bottom_panel").text == 'Завершить EUR-000000362'
    # driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").click()
    # time.sleep(2)
    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Отсканируйте поддон'
    # driver.back()
    # assert driver.find_element(AppiumBy.ID,
    #                            "android:id/message").text == 'Завершить приемку ожидаемого поступления? (все товары приняты)'
    # driver.find_element(AppiumBy.ID, "android:id/button1").click()
    # assert driver.find_element(AppiumBy.ID,
    #                            "ru.axelot.wmsx5:id/user_name").text == 'Привет, 1!'

    # for i in range(1,5) :
    #     try:
    #         driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']").click()
    #     except:
    #
    #         continue
    # driver.find_element(AppiumBy.XPATH,
    #                     "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']"). is
    # time.sleep(3)
    # driver.swipe(100,100, 100, 1000)
    # click_on_coordinates(driver, 100,500, 100, 800)
    # browser.all((AppiumBy.ID,"ru.axelot.mobileupdater:id/config_title")).element_by(have.exact_text("TG_WMS_X5_Release")).click()

    # browser.perform(command.js.scroll_into_view)
    # actions = ActionChains(browser.driver)
    # actions.scroll_by_amount(1000,2000)
    # actions.click(
    #     browser.element((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")))

    # time.sleep(10)
    # browser.with_(scroll_down_w3c()).element((AppiumBy.XPATH,"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")).click()
    # elems = browser.all((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title']"))

    # for i in elems:
    #    ...
    # print(i.get(query.text))
    # print(elems.get(query.text))
    time.sleep(5)
    # browser.element(AppiumBy.xpath("//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']")).click()

    #
    # browser.element(by.xpath("//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")).perform(command.js.scroll_into_view).click()
    # #print(elem_2)
    # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/project_title")).element(("WMS X5")).click()
    # browser.element(AppiumBy.ID, "ru.axelot.mobileupdater:id/config_title").
    # .should(have.text("WMS_FSlogistics_TST"))
    # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/project_title", texts("WMS X5"))).click()
    # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/config_title", texts("WMS_FSlogistics_TST"))).click()
    # time.sleep(60)


