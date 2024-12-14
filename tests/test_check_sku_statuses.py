import time
import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from config.base_page import BasePage
from conftest import mobile_management
import pytest



@allure.tag("Внутренние операции")
@allure.severity(Severity.NORMAL)
@allure.id("6675")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Контроль состояния объектов хранения")
@allure.story("Контроль состояния объектов хранения - базовые настройки, МУ Основная и по СГ")
def test_check_sku_statuses(mobile_management):
    driver = mobile_management

    driver.implicitly_wait(50)
    base_page = BasePage(driver)
    try:
        with allure.step("Авторизация в Axelot Start"):
            base_page.authorization_start()
            time.sleep(3)
        with allure.step("Поиск нужной базы в списке доступных баз"):
            base_page.scroll_into_veiw_base_and_click('WMSBaseTestDI')
        with allure.step("Авторизация в МК3 (1/1)"):
            base_page.authorization_MK('1', '1')
            time.sleep(4)
        with allure.step("Открыть ОЗ «Контроль состояния объектов хранения» в меню «Регламент»"):
            base_page.select_task_queue('Регламент', 'Контроль состояния объектов хранения')
        with allure.step("Проверка того, что очередь открылась успешно"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'поддон'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объект хранения'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Состояние'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/new_state_value").text == 'Брак'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '0'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 0 '
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Отсканируйте поддон'
        with allure.step("Отсканировать ШК МХ EUR-000000089"):
            base_page.type_value('EUR-000000089')
        with allure.step("Проверка перехода к следующему полю"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите объект хранения'
        with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623, которому требуется изменить состояние"):
            base_page.type_value('2704065335623')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/get_location_value").text == 'EUR-000000089'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '15012019'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '28000'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 28000 Флакон'
        with allure.step("Проверка перехода к следующему полю"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Подтвердите партию'
        with allure.step("Подтвердить партию 15012019"):
            base_page.enter_quantity('15012019')
        with allure.step("Проверка перехода к следующему полю"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Введите количество'
        with allure.step("Ввести количество 5"):
            base_page.type_value('5')
            assert driver.find_element(AppiumBy.ID,
                                       "ru.axelot.wmsx5:id/qty_value").text == '5'
        with allure.step("Проверка перехода к следующему полю"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Выберите состояние'
        with allure.step("Выбрать новое состояния 'Брак'"):
            base_page.select_value_from_list('Брак')
        with allure.step("Проверка того, что задача выполнилась успешно"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'поддон'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Объект хранения'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Состояние'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/new_state_value").text == 'Брак'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/qty_value").text == '0'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 0 '
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Отсканируйте поддон'

    except Exception as ex:
        print(ex)
        allure.attach(
            mobile_management.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
