import time

import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy

from config.base_page import BasePage
from conftest import mobile_management


@pytest.mark.БыстрыйЦикл
@allure.tag("Внутренние операции")
@allure.severity(Severity.NORMAL)
@allure.id("6481")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Перемещение ОХ")
@allure.story("Перемещение ОХ - базовые настройки, МУ партии")
def test_sku_movement(mobile_management):
    driver = mobile_management
    driver.implicitly_wait(50)
    base_page = BasePage(driver)
    try:
        with allure.step("Авторизация в Axelot Start"):
            base_page.authorization_start()
            time.sleep(5)
        with allure.step("Поиск нужной базы в списке доступных баз"):
            base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
        with allure.step("Авторизация в МК3 (1/1)"):
            base_page.authorization_MK('1', '1')
            time.sleep(6)
        with allure.step("Открыть ОЗ «Перемещение ОХ (базовые настройки)» в меню «Перемещение»."):
            base_page.select_task_queue('Перемещение', 'Перемещение ОХ (базовые настройки)')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == '2-4-3-1'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location2_value").text == 'EUR-000000118'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '18012023'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 50 Флакон'
        with allure.step("Отсканировать ШК ячейки-источника 2-4-3-1"):
            base_page.type_value('2431')
        with allure.step("Отсканировать ШК поддона-источника EUR-000000118"):
            base_page.type_value('EUR-000000118')
        with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
            base_page.type_value('2704065335623')
        with allure.step("Подтвердить партию 18012023"):
            base_page.enter_quantity('18012023')
        with allure.step("Ввести количество по плану."):
            base_page.type_value('50')
        with allure.step("Отсканировать МХ размещения EUR-000000099"):
            base_page.type_value('EUR-000000099')
        with allure.step("Получение всплывающей формы 'Получение задач' и выход к списку ОЗ"):
            base_page.assert_finish_sku_picking()

    except Exception as ex:
        print(ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise