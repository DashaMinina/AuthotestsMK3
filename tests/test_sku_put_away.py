import time
import allure
import pytest

from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy


from config.appium_utils import initialize_appium_driver
from config.base_page import BasePage

@pytest.mark.БыстрыйЦикл
@allure.tag("Входящий поток")
@allure.severity(Severity.CRITICAL)
@allure.id("#6188")
@allure.label("owner", "Daria Tomilova")
@allure.feature("Размещение по составу (раскладывание)")
@allure.story("Размещение по составу - расширенные настройки, МУ Основная и по СГ")
def test_sku_put_away():
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
        with allure.step("В главном меню выбрать пункт «Размещение», переходит в ОЗ «Размещение по составу (базовые настройки)»;"):
            base_page.select_task_queue('Размещение', 'Размещение по составу (базовые настройки)')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position1_value").text == 'DOC-1'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/position_value").text == 'EUR-000000320'
        with allure.step("Отсканировать ШК указанного на ТСД МХ EUR-000000320"):
            base_page.type_value('EUR-000000320')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Средство для чистки объективов'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/batch_value").text == '19092024'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 Флакон'
        with allure.step("Отсканировать ШК ОХ 'Средство для чистки объективов' 2704065335623."):
            base_page.type_value('2704065335623')
        with allure.step("Отсканировать ШК ячейки размещения из подсказки 1-1-2-1"):
            base_page.type_value('1121')
        with allure.step("Отсканировть ШК поддона размещения из подсказки EUR-000000092"):
            base_page.type_value('EUR-000000092')
        with allure.step("Ввести размещаемое количество по плану 100."):
            base_page.type_value('100')
        with allure.step("Проверка значений в полученной задаче"):
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/sku_value").text == 'Наушники'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/state_value").text == 'Годен'
            assert driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/total_qty_package").text == '0 / 100 шт'
        with allure.step("Отсканировать ШК ОХ 'Наушники' 2620424001643."):
            base_page.type_value('2620424001643')
        with allure.step("Отсканировать ШК ячейки размещения из подсказки 1-1-2-1"):
            base_page.type_value('1121')
        with allure.step("Отсканировать ШК поддона размещения из подсказки EUR-000000092"):
                base_page.type_value('EUR-000000092')
        with allure.step("Ввести размещаемое количество по плану 100."):
            base_page.type_value('100')

    except Exception as ex:
        print(ex)
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот ошибки",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    # finally:
    #     # не работает, приложение остается открытым
    #     driver.close()
    #     driver.quit()