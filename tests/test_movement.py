import time

import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy

from config.base_page import BasePage
from conftest import mobile_management


@pytest.mark.БыстрыйЦикл
@allure.tag("Внутренние операции")
@allure.severity(Severity.CRITICAL)
@allure.id("6482")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Перемещение МХ")
@allure.story("Перемещение МХ - базовые настройки")
def test_movement(mobile_management):
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
        with allure.step("Открыть ОЗ «Перемещение (базовые настройки)»"):
            base_page.select_task_queue('Перемещение', 'Перемещение (базовые настройки)')
        with allure.step("Отсканировать ШК МХ EUR-000000342"):
            base_page.type_value('EUR-000000342')
        with allure.step("Проверка значений в выполняемой задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == '2-4-1-4'
        with allure.step("Отсканировать ячейку размещения 2-4-1-4"):
            base_page.type_value('2414')
        with allure.step("Получена следующая задача DOC1/EUR-000000314"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-1'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000314'
    except Exception as ex:
        print(ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise

