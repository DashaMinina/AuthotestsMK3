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
@allure.id("6191")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Контроль поступления по составу")
@allure.story("Контроль поступления по составу - базовые настройки, МУ Основная и по СГ")
def test_receipt_check_by_lines(mobile_management):
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
        with allure.step("Открыть ОЗ «Контроль поступления по составу (базовые настройки)» в меню «Приемка»."):
            base_page.select_task_queue('Приемка', 'Контроль поступления по составу (базовые настройки)')
        with allure.step("Отсканировать ШК МХ для пересчета EUR-000000321, указанный на ТСД."):
            base_page.type_value('EUR-000000321')
        with allure.step("Отсканировать ШК ОХ 'Наушники' 2620424001643."):
            base_page.type_value('2620424001643')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000321'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Наушники'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 шт'
        with allure.step("Ввести количество по плану."):
            base_page.type_value('100')
        with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
            base_page.type_value('2704065335623')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location_value").text == 'EUR-000000321'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '18092024'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 Флакон'
        with allure.step("Выбрать партию '18092024' из списка."):
            base_page.type_value('18092024')
        with allure.step("Ввести количество 100"):
            base_page.type_value('100')
        with allure.step("Завершить пересчет МХ по кнопке «Завершить» в «Меню»."):
            base_page.finish_task_in_menu()
        with allure.step("Получение всплывающей формы 'Получение задач' и выход к списку ОЗ"):
            base_page.assert_finish_sku_picking()
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
        # with allure.step("Подтверждение расхождений."):
        #     base_page.finish_receipt_by_lines_with_discrepancies()

    except Exception as ex:
        print(ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
