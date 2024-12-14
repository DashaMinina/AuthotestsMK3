import time
import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from config.base_page import BasePage
from conftest import mobile_management
import pytest



@allure.tag("Исходящий поток")
@allure.severity(Severity.CRITICAL)
@allure.id("6674")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Контроль отгрузки по составу")
@allure.story("Контроль отгрузки по составу - МУ Основная и по СГ")
def test_dispatch_check_by_sku(mobile_management):
    driver = mobile_management

    driver.implicitly_wait(50)
    base_page = BasePage(driver)
    try:
        # with allure.step("Авторизация в Axelot Start"):
        #     base_page.authorization_start()
        #     time.sleep(3)
        # with allure.step("Поиск нужной базы в списке доступных баз"):
        #     base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
        with allure.step("Авторизация в МК3 (1/1)"):
            base_page.authorization_MK('1', '1')
            time.sleep(4)
        with allure.step("Открыть ОЗ «Контроль отгрузки по составу» в меню «Отгрузка»"):
            base_page.select_task_queue('Отгрузка', 'Контроль отгрузки по составу')
        # with allure.step("Проверка того, что получена задача по МХ EUR-000000343"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000343'
        # with allure.step("Отсканировать ШК МХ для пересчета EUR-000000343, указанный на ТСД"):
        #     base_page.type_value('EUR-000000343')
        # with allure.step("Проверка перехода к следующему полю"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите объект хранения'
        # with allure.step("Отсканировать ШК ОХ 'Объектив' 2145806977489"):
        #     base_page.type_value('2145806977489')
        # with allure.step("Проверка значений в полученной задаче"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location_value").text == 'EUR-000000343'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объектив'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == 'TR2_190429'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 75 шт'
        # with allure.step("Проверка перехода к следующему полю"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Подтвердите партию'
        # with allure.step("Отсканировать партию TR2_190429"):
        #     base_page.type_value('TR2_190429')
        # with allure.step("Проверка перехода к следующему полю"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите количество'
        # with allure.step("Ввести количество по плану 75"):
        #      base_page.type_value('75')
        # with allure.step("Проверка перехода к вводу следующего ОХ"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объект хранения'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Состояние'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '0'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 0 '
        #     assert driver.find_element(AppiumBy.ID,
        #                                "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите объект хранения'
        # with allure.step("Отсканировать ШК ОХ 'Усилитель' 2507812345407"):
        #     base_page.type_value('2507812345407')
        # with allure.step("Проверка значений в полученной задаче"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000343'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Усилитель'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 75 шт'
        # with allure.step("Проверка перехода к следующему полю"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите количество'
        # with allure.step("Ввести количество по плану 75"):
        #      base_page.type_value('75')
        # with allure.step("Проверка перехода к вводу следующего ОХ"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объект хранения'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Состояние'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '0'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 0 '
        #     assert driver.find_element(AppiumBy.ID,
        #                                "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите объект хранения'
        # with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
        #     base_page.type_value('2704065335623')
        # with allure.step("Проверка значений в полученной задаче"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location_value").text == 'EUR-000000343'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '25092024'
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 75 Флакон'
        # with allure.step("Проверка перехода к следующему полю"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Подтвердите партию'
        # with allure.step("Отсканировать партию 25092024"):
        #     base_page.type_value('25092024')
        # with allure.step("Проверка перехода к следующему полю"):
        #     assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите количество'
        # with allure.step("Ввести количество 75"):
        #     base_page.type_value('75')
        # with allure.step("Завершить пересчет МХ по кнопке «Завершить» в «Меню»."):
        #     base_page.finish_task_in_menu()
        # with allure.step("Получение всплывающей формы 'Получение задач' и выход к списку ОЗ"):
        #     base_page.assert_finish_sku_picking()

    except Exception as ex:
        print(ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
