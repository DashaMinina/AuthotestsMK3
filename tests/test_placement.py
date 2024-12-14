import time

import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy

from config.base_page import BasePage
from conftest import mobile_management


@pytest.mark.БыстрыйЦикл
@allure.tag("Входящий поток")
@allure.severity(Severity.CRITICAL)
@allure.id("6357")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Размещение")
@allure.story("Размещение МХ - базовые настройки")
def test_placement(mobile_management):
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
        with allure.step("Открыть ОЗ «Размещение МХ (базовые настройки)» в меню «Размещение»."):
            base_page.select_task_queue('Размещение', 'Размещение МХ (базовые настройки)')
        with allure.step("Отсканировать ШК указанного на ТСД МХ (EUR-000000314)."):
            base_page.type_value('EUR-000000314')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'B-2-1'
        with allure.step("Отсканировать ШК ячейки размещения (B21)."):
            base_page.type_value('B21')
        with allure.step("Проверка значений в новой полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000315'
        with allure.step("Отсканировать ШК указанного на ТСД МХ (EUR-000000315)."):
            base_page.type_value('EUR-000000315')
        with allure.step("Проверка значений в новой полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'B-2-2'
        with allure.step("Отсканировать ШК ячейки размещения (B22)."):
            base_page.type_value('B22')
        with allure.step("Проверка значений в новой полученной задаче"):
            base_page.assert_finish_sku_picking()

    except Exception as ex:
        print (ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    # finally:
    #     driver.quit()



