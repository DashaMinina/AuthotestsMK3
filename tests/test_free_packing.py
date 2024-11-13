import time
import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage


@allure.tag("Исходящий поток")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Tomilova")
@allure.feature("Упаковка")
@allure.story("Свободная упаковка - базовые настройки, МУ Основная, по партиям и по СГ")
def test_free_packing():
    driver = initialize_appium_driver()
    driver.implicitly_wait(50)
    base_page = BasePage(driver)
    with allure.step("Проходит процедуру авторизации в Axelot Start"):
        base_page.authorization_start()
        time.sleep(5)
    with allure.step("Поиск нужной базы в списке доступных баз"):
        base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
    with allure.step("Проходит процедуру авторизации в МК3"):
        base_page.authorization_MK('1', '1')
        time.sleep(6)
    with allure.step("Открывает ОЗ «Свободная упаковка (базовые настройки)»"):
        base_page.select_task_queue('Отгрузка', 'Свободная упаковка (базовые настройки)')
    with allure.step("Выбирает ЗнО 00000000003 из списка."):
        base_page.select_document('Заказ на отгрузку 00000000003 от 25.09.2024')
    with allure.step("Сканирует ШК МХ источника с отобранными ОХ EUR-000000343, откуда производится упаковка."):
        base_page.type_value('EUR-000000343')
    with allure.step("Сканирует ШК ОХ 'Объектив' 2145806977489."):
        base_page.type_value('2145806977489')
    with allure.step("Проверка значений в полученной задаче"):
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объектив'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == 'TR2_190429'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 75 шт'
    with allure.step("Подтверждает партию TR2_190429"):
        base_page.enter_quantity('TR2_190429')
    with allure.step("Вводит ШК нового МХ приемника EUR-000000344, в который производится упаковка."):
        base_page.type_value('EUR-000000344')
    with allure.step("Вводит ячейку PK1"):
        base_page.type_value('PK1')
    with allure.step("Вводит количество по плану (75)"):
        base_page.type_value('75')
    with allure.step("Сканирует ШК ОХ 'Усилитель' 2507812345407."):
        base_page.type_value('2507812345407')
    with allure.step("Проверка значений в полученной задаче"):
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Усилитель'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 75 шт'
    with allure.step("Вводит ШК МХ приемника EUR-000000344, в который производится упаковка."):
        base_page.type_value('EUR-000000344')
    with allure.step("Вводит количество по плану (75)"):
        base_page.type_value('75')
    with allure.step("Сканирует ШК ОХ 'Средство для чистки объективов' 2704065335623."):
        base_page.type_value('2704065335623')
    with allure.step("Проверка значений в полученной задаче"):
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '25092024'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 75 Флакон'
    with allure.step("Подтверждает партию 25092024"):
        base_page.enter_quantity('25092024')
    with allure.step("Вводит ШК МХ приемника EUR-000000344, в который производится упаковка."):
        base_page.type_value('EUR-000000344')
    with allure.step("Вводит количество по плану (75)"):
        base_page.type_value('75')
    with allure.step("Завершаем упаковку нажатием кнопки «Завершить»."):
        base_page.finish_task_in_menu()
    with allure.step("Подтверждение расхождений."):
        base_page.type_value('EUR-000000344')
