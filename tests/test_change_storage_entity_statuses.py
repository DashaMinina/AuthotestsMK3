import time
import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from config.base_page import BasePage
from conftest import mobile_management
import pytest



@allure.tag("Внутренние операции")
@allure.severity(Severity.NORMAL)
@allure.id("6673")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Изменение состояния мест хранения")
@allure.story("Изменение состояния мест хранения")
def test_change_storage_entity_statuses(mobile_management):
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
        with allure.step("Открыть ОЗ «Изменение состояния мест хранения» в меню «Регламент»"):
            base_page.select_task_queue('Регламент', 'Изменение состояния мест хранения')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == '1-1-1-4'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/location_value").text == 'EUR-000000087'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Доступно'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Отсканируйте поддон'
        with allure.step("Отсканировать ШК МХ EUR-000000087"):
            base_page.type_value('EUR-000000087')
        with allure.step("Проверка перехода к следующему полю"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/textHint_bottom_panel").text == 'Выберите состояние'
        with allure.step("Выбрать новое состояния 'Заблокировано'"):
            base_page.select_value_from_list('Заблокировано')
        with allure.step("Подтверждение смены состояния МХ на Заблокировано"):
            assert driver.find_element(AppiumBy.ID,
                                       "android:id/alertTitle").text == 'Подтверждение выполнения'
            assert driver.find_element(AppiumBy.ID,
                                       "android:id/message").text == 'Установить для EUR-000000087 состояние Заблокировано?'
            driver.find_element(AppiumBy.ID, "android:id/button1").click()
        with allure.step("Получение всплывающей формы 'Получение задач' и выход к списку ОЗ"):
            base_page.assert_finish_sku_picking()

    except Exception as ex:
        print(ex)
        allure.attach(
            mobile_management.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
