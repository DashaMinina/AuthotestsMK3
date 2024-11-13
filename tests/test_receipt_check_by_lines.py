import time
import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage


@allure.tag("Входящий поток")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Tomilova")
@allure.feature("Контроль поступления по составу")
@allure.story("Контроль поступления по составу - базовые настройки, МУ Основная и по СГ")
def test_receipt_check_by_lines():
    # Нужно переработать ассерты на отображение ячейки и ввод ячейки Doc-1 (на момент написания теста была блок ошибка)
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
    with allure.step("Открывает ОЗ «Контроль поступления по составу (базовые настройки)» в меню «Приемка»."):
        base_page.select_task_queue('Приемка', 'Контроль поступления по составу (базовые настройки)')
    with allure.step("Проверка значений в полученной задаче"):
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000321'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Наушники'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 шт'
    with allure.step("Сканирует ШК МХ для пересчета EUR-000000321, указанный на ТСД."):
        base_page.type_value('EUR-000000321')

    with allure.step("Сканирует ШК МХ для пересчета EUR-000000321, указанный на ТСД."):
        base_page.type_value('EUR-000000321')

    with allure.step("Сканирует ШК ОХ 'Наушники' 2620424001643."):
        base_page.type_value('2620424001643')

    with allure.step("Вводит количество по плану."):
        base_page.type_value('100')
    with allure.step("Проверка значений в полученной задаче"):
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000321'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '18092024'
        assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 Флакон'
    with allure.step("Сканирует ШК ОХ 'Средство для чистки объективов' 2704065335623."):
        base_page.type_value('2704065335623')
        time.sleep(1)
    with allure.step("Выбирает партию '18092024' из списка."):
        base_page.type_value('18092024')
    with allure.step("Вводит количество на 1 больше, чем в подсказке (101)."):
        base_page.type_value('101')
    with allure.step("Завершает пересчет МХ по кнопке «Завершить» в «Меню»."):
        base_page.finish_task_in_menu()
    # with allure.step("Проверка формы завершения пересчета с расхождениями"):
    #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/report_title").text == 'Завершить пересчет с отклонениями?'
    #     assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/report_row_title").text == 'EUR-000000321'
    #     assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/child_report_title").text == 'Наушники'
    #     assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/child_report_qty").text == '100'
    #     assert driver.find_element(AppiumBy.ID,"ru.axelot.wmsx5:id/child_report_qty_plan").text == '/100'
    #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/report_row_title").text == 'EUR-000000321'
    #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/child_report_title").text == 'Наушники'
    #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/child_report_qty").text == '100'
    #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/child_report_qty_plan").text == '/100'
    with allure.step("Подтверждение расхождений."):
        base_page.finish_receipt_by_lines_with_discrepancies()