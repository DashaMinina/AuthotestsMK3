import time

import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage

@pytest.mark.БыстрыйЦикл
@allure.tag("Исходящий поток")
@allure.severity(Severity.CRITICAL)
@allure.id("#6356")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Отгрузка")
@allure.story("Отгрузка - базовые настройки")
def test_shipping():
    driver = initialize_appium_driver()
    driver.implicitly_wait(50)
    base_page = BasePage(driver)
    try:
        with allure.step("Авторизация в Axelot Start"):
            base_page.authorization_start()
            time.sleep(5)
        with allure.step("Поиск нужной базы в списке доступных баз"):
            base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
        with allure.step("Авторизация в МК3"):
            base_page.authorization_MK('1', '1')
            time.sleep(6)
        with allure.step("Открыть ОЗ «Отгрузка (базовые настройки)» в меню «Отгрузка»."):
            base_page.select_task_queue('Отгрузка', 'Отгрузка (базовые настройки)')
        with allure.step("Выбрать ДО, по которому будет выполняться отгрузка (00000000004)"):
            base_page.select_document('Заказ на отгрузку 00000000004 от 25.09.2024')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-2'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000350'
        with allure.step("Отсканировать ШК отгружаемого места хранения (EUR-000000350)"):
            base_page.type_value('EUR-000000350')
        with allure.step("Подтвердить отгрузку места хранения"):
            assert driver.find_element(AppiumBy.ID, "android:id/alertTitle").text == 'Подтверждение выполнения'
            assert driver.find_element(AppiumBy.ID, "android:id/message").text == 'Грузовое место EUR-000000350 отгружено?'
            driver.find_element(AppiumBy.ID, "android:id/button1").click()
        # with allure.step("Получение всплывающей формы 'Получение задач' и выход к списку ОЗ"):
        #     base_page.assert_finish_shipping()
    except Exception as ex:
        print (ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise



    # assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-2'
    # base_page.type_value('DOC2')
    # base_page.assert_finish_sku_picking()
    # time.sleep(2)