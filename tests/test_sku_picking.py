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
@allure.id("6359")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Отбор ОХ")
@allure.story("Отбор ОХ - базовые настройки, МУ Основная")
def test_sku_picking(mobile_management):
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
        with allure.step("Открыть ОЗ «Отбор ОХ (базовые настройки)» в меню «Отбор»."):
            base_page.select_task_queue('Отбор', 'Отбор ОХ (базовые настройки)')
        with allure.step("Отсканировать ШК нового МХ для сборки заказа (EUR-000000332)."):
            assert driver.find_element(AppiumBy.ID,
                                       "ru.axelot.wmsx5:id/textViewTip").text == 'Введите место хранения для отбора Заказ на отгрузку № 00000000001 от 25.09.2024'
            base_page.type_value('EUR-000000332')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == '2-4-2-1'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location2_value").text == 'EUR-000000331'
            assert driver.find_element(AppiumBy.ID,
                                       "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '25092024'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 70 Флакон'

        with allure.step("Отсканировать ШК МХ, из состава ячейки, с которого происходит отбор (EUR-000000331)"):
            base_page.type_value('EUR-000000331')

        with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
            base_page.type_value('2704065335623')
        with allure.step("Выбирает партию '25092024м' из списка."):
            base_page.type_value('25092024')
        with allure.step("Ввести количество по плану (70)."):
            base_page.type_value('70')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == '1-1-3-1'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location2_value").text == 'EUR-000000330'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Наушники'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 55 шт'
        with allure.step("Отсканировать ШК МХ, из состава ячейки, с которого происходит отбор (EUR-000000330)"):
            base_page.type_value('EUR-000000330')
        with allure.step("Отсканировать ШК ОХ 'Наушники' 2620424001643."):
            base_page.type_value('2620424001643')
        with allure.step("Ввести количество по плану (55)."):
            base_page.type_value('55')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-2'
        with allure.step("На операции «Положить» отсканировать ШК ячейки зоны ворот отгрузки (DOC-2)"):
            base_page.type_value('DOC2')
        with allure.step("Получение всплывающей формы 'Получение задач' и выход к списку ОЗ"):
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