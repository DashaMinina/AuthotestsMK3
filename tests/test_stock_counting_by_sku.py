import time
import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage

@pytest.mark.БыстрыйЦикл
@allure.tag("Внутренние операции")
@allure.severity(Severity.CRITICAL)
@allure.id("6189")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Инвентаризация состава")
@allure.story("Инвентаризация состава - базовые настройки, МУ Основная и по СГ")
def test_stock_counting_by_sku():
    driver = initialize_appium_driver()
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
        with allure.step("Открыть ОЗ «Инвентаризация состава (базовые настройки)» в меню «Регламент»."):
            base_page.select_task_queue('Регламент', 'Инвентаризация состава (базовые настройки)')
        with allure.step("Отсканировать ШК ячейки 1-1-3-1"):
            base_page.type_value('1131')
        with allure.step("Отсканировать ШК МХ, которое находится в ячейке EUR-000000111"):
            base_page.type_value('EUR-000000111')
        with allure.step("Отсканировать ШК ОХ 'Наушники' 2620424001643."):
            base_page.type_value('2620424001643')
        with allure.step("Ввести плановое количество товара"):
            base_page.type_value('100')
        with allure.step("Отсканировать ШК МХ, которое находится в ячейке EUR-000000111"):
            base_page.type_value('EUR-000000111')
        with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
            base_page.type_value('2704065335623')
            time.sleep(1)
        with allure.step("Выбрать партию '18092024' из списка."):
            base_page.type_value('18092024')
        with allure.step("Ввести плановое количество товара"):
            base_page.type_value('101')
        with allure.step("Завершить инвентаризацию («Меню» - «Завершить инвентаризацию»)."):
            base_page.finish_task_in_menu()
        with allure.step("Проверка на наличие формы 'Не найдено задач. Повторить поиск задач?'"):
            base_page.assert_finish_sku_picking()
    except Exception as ex:
        print(ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
