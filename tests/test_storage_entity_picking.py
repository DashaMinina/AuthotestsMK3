import time

import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy

from config.base_page import BasePage
from conftest import mobile_management


@pytest.mark.БыстрыйЦикл
@allure.tag("Исходящий поток")
@allure.severity(Severity.CRITICAL)
@allure.id("6358")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Отбор МХ")
@allure.story("Отбор МХ - базовые настройки")
def test_storage_entity_picking(mobile_management):
    driver = mobile_management
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
        with allure.step("Открыть ОЗ «Отбор МХ (базовые настройки)» в меню «Отбор»."):
            base_page.select_task_queue('Отбор', 'Отбор МХ (базовые настройки)')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/position1_value").text == '1-1-2-4'
            assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/position_value").text == 'EUR-000000338'
        with allure.step("Отсканировать ШК отбираемого МХ (EUR-000000338)."):
            base_page.type_value('EUR-000000338')
        with allure.step("Проверка перехода на шаг 'Положить', подсказка с ячейкой размещения"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-2'
        with allure.step("На операции «Положить» отсканировать ШК ячейки зоны завершения отбора (DOC2)"):
            base_page.type_value('DOC2')

        with allure.step("Получение всплывающей формы 'Получение задач' и выход к списку ОЗ"):
            base_page.assert_finish_sku_picking()
# перенести обработку скриншота в yeild
    except Exception as ex:
        print (ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
