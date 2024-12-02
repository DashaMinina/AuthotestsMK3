import time

import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selene import browser, command
from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage
from config.conftest import mobile_management


#потом обернуть авторизацию в фикстуру и перенести в confest
@pytest.mark.БыстрыйЦикл
@allure.tag("Входящий поток")
@allure.severity(Severity.CRITICAL)
@allure.id('#6194')
@allure.label("owner", "Daria Tomilova")
@allure.feature("Приемка (пересчет)")
@allure.story("Приемка (пересчет) - базовые настройки, МУ Основная и по СГ")
def test_check_in_counting():
    driver = mobile_management()
    driver.implicitly_wait(50)
    base_page = BasePage(driver)
    with allure.step("Авторизация в Axelot Start"):
        base_page.authorization_start()
        time.sleep(5)
    with allure.step("Поиск нужной базы в списке доступных баз"):
        base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
    with allure.step("Авторизация в МК3 (1/1)"):
        base_page.authorization_MK('1', '1')
        time.sleep(6)
    with allure.step("Открыть ОЗ «Приемка (базовые настройки)» в меню «Приемка»."):
        base_page.select_task_queue('Приемка', 'Приемка (базовые настройки)')
    with allure.step("Выбрать документ «Ожидаемое поступление 00000000003» из списка."):
        base_page.select_document('Ожидаемое поступление 00000000003 от 19.09.2024')
    with allure.step("Отсканировать ШК ячейки, в которой будет выполняться приемка DOC1."):
        base_page.type_value('DOC1')
    with allure.step("Отсканировать ШК ранее сгенерированного МХ EUR-000000305."):
        base_page.type_value('EUR-000000305')
    with allure.step("Отсканировать ШК ОХ 'Кабель микрофонный' 2227930983724."):
        base_page.type_value('2227930983724444444444')
    with allure.step("Проверка значений в полученной задаче"):
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Кабель микрофонный'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '100'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 пач.'
    with allure.step("Ввести количество принимаемых ОХ по плану (100)."):
        base_page.type_value('100')
    with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
        base_page.type_value('2704065335623')
    with allure.step("Проверка значений в полученной задаче"):
        assert driver.find_element(AppiumBy.ID,
                                   "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 1000 Флакон'
    with allure.step("Отсканировать партию 18092024."):
        base_page.type_value('18092024')
    with allure.step("Ввести количество принимаемых ОХ по плану (1000)."):
        base_page.type_value('1000')
    with allure.step("Завершить пересчет МХ по кнопке «Завершить» в «Меню»."):
        base_page.finish_task_in_menu()
    with allure.step("Завершить приемку по ОП"):
        base_page.finish_check_in_counting()



#         переписать, не выходит  из очереди, не нажимается driver.back()
    # try:
    #     with allure.step("Авторизация в Axelot Start"):
    #         base_page.authorization_start()
    #         time.sleep(5)
    #     with allure.step("Поиск нужной базы в списке доступных баз"):
    #         base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
    #     with allure.step("Авторизация в МК3 (1/1)"):
    #         base_page.authorization_MK('1', '1')
    #         time.sleep(6)
    #     with allure.step("Открыть ОЗ «Приемка (базовые настройки)» в меню «Приемка»."):
    #         base_page.select_task_queue('Приемка', 'Приемка (базовые настройки)')
    #     with allure.step("Выбрать документ «Ожидаемое поступление 00000000003» из списка."):
    #         base_page.select_document('Ожидаемое поступление 00000000003 от 19.09.2024')
    #     with allure.step("Отсканировать ШК ячейки, в которой будет выполняться приемка DOC1."):
    #         base_page.type_value('DOC1')
    #     with allure.step("Отсканировать ШК ранее сгенерированного МХ EUR-000000305."):
    #         base_page.type_value('EUR-000000305')
    #     with allure.step("Отсканировать ШК ОХ 'Кабель микрофонный' 2227930983724."):
    #         base_page.type_value('2227930983724')
    #     with allure.step("Проверка значений в полученной задаче"):
    #         assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Кабель микрофонный'
    #         assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    #         assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '100'
    #         assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 пач.'
    #     with allure.step("Ввести количество принимаемых ОХ по плану (100)."):
    #         base_page.type_value('100')
    #     with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
    #         base_page.type_value('2704065335623')
    #     with allure.step("Проверка значений в полученной задаче"):
    #         assert driver.find_element(AppiumBy.ID,
    #                                    "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
    #         assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
    #         assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 1000 Флакон'
    #     with allure.step("Отсканировать партию 18092024."):
    #         base_page.type_value('18092024')
    #     with allure.step("Ввести количество принимаемых ОХ по плану (1000)."):
    #         base_page.type_value('1000')
    #     with allure.step("Завершить пересчет МХ по кнопке «Завершить» в «Меню»."):
    #         base_page.finish_task_in_menu()
    #     with allure.step("Завершить приемку по ОП"):
    #         base_page.finish_check_in_counting()
    # #         переписать, не выходит  из очереди, не нажимается driver.back()
    #
    #
    #
    # except Exception as ex:
    #     print(ex)
    #     allure.attach(
    #         driver.get_screenshot_as_png(),
    #         name="Скриншот ошибки",
    #         attachment_type=allure.attachment_type.PNG
    #     )
    #     raise




# def test_receipt():
#     # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/login_edit")).type('admin')
#     # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/password_edit")).type('admin')
#     # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/address_edit")).type('192.168.101.9:5275')
#     # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/connect_button")).click()
#     # time.sleep(1)
#     # browser.element((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']")).click()
#     driver = initialize_appium_driver()
#     driver.implicitly_wait(50)
#     # driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/login_edit").send_keys('admin')
#     # driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/password_edit").send_keys('admin')
#     # driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/address_edit").send_keys('192.168.101.9:5275')
#     driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/connect_button").click()
#     # driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']").click()
#     time.sleep(6)
#     start_x = 200
#     start_y = 600
#     end_x = 200
#     end_y = 100
#     duration = 400  # Время анимации свайпа в миллисекундах
#     driver.swipe(start_x, start_y, end_x, end_y, duration)
#     driver.swipe(start_x, start_y, end_x, end_y, duration)
#     driver.swipe(start_x, start_y, end_x, end_y, duration)
#     driver.swipe(start_x, start_y, end_x, end_y, duration)
#
#     driver.find_element(AppiumBy.XPATH,
#                         "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='WMSBaseTestDI']").click()
#     driver.find_element(AppiumBy.XPATH,
#                         "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='WMSBaseTestDI']").click()
#
#     # driver.find_element(AppiumBy.ID, "android:id/button1").click()
#     # driver.wait_activity(driver.find_element(AppiumBy.ID, "android:id/button1"))
#     # time.sleep(200)
#     # driver.wait_activity(driver.find_element(AppiumBy.ID, "android:id/button1").click())
#     # time.sleep(60)
#     # driver.wait_activity(driver.find_element(AppiumBy.ID, "com.miui.global.packageinstaller:id/btn_open_normal").click())
#     # time.sleep(40)
#
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/login_input").send_keys('1')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/password_input").send_keys('1')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/connect_button").click()
#     time.sleep(6)
#     driver.find_element(AppiumBy.XPATH,
#                         "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Приемка']").click()
#     driver.find_element(AppiumBy.XPATH,
#                         "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='Приемка (базовые настройки)']").click()
#     driver.find_element(AppiumBy.XPATH,
#                         "//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/document_title' and @text='Ожидаемое поступление 00000000003 от 19.09.2024']").click()
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('DOC1')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     time.sleep(2)
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('EUR-000000305')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     time.sleep(2)
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('2227930983724')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     time.sleep(2)
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Кабель микрофонный'
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '100'
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 пач.'
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('100')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     time.sleep(2)
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('2867549627970')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     time.sleep(2)
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 1000 Флакон'
#     time.sleep(2)
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('18092024')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys('1000')
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/floatingActionButton").click()
#     time.sleep(2)
#     # assert driver.find_element(AppiumBy.ID,
#     #                                "ru.axelot.wmsx5:id/editText_bottom_panel").text == 'Завершить EUR-000000362'
#     driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").click()
#     time.sleep(2)
#     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Отсканируйте поддон'
#     driver.back()
#     assert driver.find_element(AppiumBy.ID,
#                                "android:id/message").text == 'Завершить приемку ожидаемого поступления? (все товары приняты)'
#     driver.find_element(AppiumBy.ID, "android:id/button1").click()
#     assert driver.find_element(AppiumBy.ID,
#                                "ru.axelot.wmsx5:id/user_name").text == 'Привет, 1!'
#
#     # for i in range(1,5) :
#     #     try:
#     #         driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']").click()
#     #     except:
#     #
#     #         continue
#     # driver.find_element(AppiumBy.XPATH,
#     #                     "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']"). is
#     # time.sleep(3)
#     # driver.swipe(100,100, 100, 1000)
#     # click_on_coordinates(driver, 100,500, 100, 800)
#     # browser.all((AppiumBy.ID,"ru.axelot.mobileupdater:id/config_title")).element_by(have.exact_text("TG_WMS_X5_Release")).click()
#
#     # browser.perform(command.js.scroll_into_view)
#     # actions = ActionChains(browser.driver)
#     # actions.scroll_by_amount(1000,2000)
#     # actions.click(
#     #     browser.element((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")))
#
#     # time.sleep(10)
#     # browser.with_(scroll_down_w3c()).element((AppiumBy.XPATH,"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")).click()
#     # elems = browser.all((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title']"))
#
#     # for i in elems:
#     #    ...
#     # print(i.get(query.text))
#     # print(elems.get(query.text))
#     time.sleep(5)
#     # browser.element(AppiumBy.xpath("//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']")).click()
#
#     #
#     # browser.element(by.xpath("//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='TG_WMS_X5_Release']")).perform(command.js.scroll_into_view).click()
#     # #print(elem_2)
#     # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/project_title")).element(("WMS X5")).click()
#     # browser.element(AppiumBy.ID, "ru.axelot.mobileupdater:id/config_title").
#     # .should(have.text("WMS_FSlogistics_TST"))
#     # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/project_title", texts("WMS X5"))).click()
#     # browser.element((AppiumBy.ID, "ru.axelot.mobileupdater:id/config_title", texts("WMS_FSlogistics_TST"))).click()
#     # time.sleep(60)
