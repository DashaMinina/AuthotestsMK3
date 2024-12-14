import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def authorization_MK(self, login, password):
        # Авторизация в МК3
        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/login_input").send_keys(login)
        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/password_input").send_keys(password)
        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/connect_button").click()
        time.sleep(2)

    def authorization_start(self,login = 'admin',password = 'admin', address = '192.168.101.9:5275'):
        # Авторизация в AxelotStart
        self.driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/login_edit").send_keys(login)
        self.driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/password_edit").send_keys(password)
        self.driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/address_edit").send_keys(address)
        self.driver.find_element(AppiumBy.ID, "ru.axelot.mobileupdater:id/connect_button").click()
        time.sleep(2)

    def scroll_into_veiw_base_and_click(self, element):
        # Найти (долистать) до нужной базы в списке и перейти по ней в AxelotStart
        # self.driver.find_element(AppiumBy.XPATH,
        #                          "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']").click()
        # self.driver.find_element(AppiumBy.XPATH,
        #                          "//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/project_title' and @text='WMS X5']").click()
        self.driver.implicitly_wait(1)
        while True:
            try:
                target_element = self.driver.find_element(
                    AppiumBy.XPATH,
                    f"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='{element}']"
                )
                if target_element.is_displayed():
                    self.driver.find_element(AppiumBy.XPATH,
                                             f"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='{element}']").click()
                    # self.driver.find_element(AppiumBy.XPATH,
                    #                          f"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text='{element}']").click()
                    break
            except NoSuchElementException:
                self.driver.swipe(start_x=200, start_y=600, end_x=200, end_y=100, duration=300)

        self.driver.implicitly_wait(50)

        # while self.driver.find_element(AppiumBy.XPATH,
        #                 f"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text={element}]").is_displayed() is False:
        #     self.driver.swipe(start_x = 200,start_y = 600,end_x = 200,end_y = 100,duration = 300)

    def select_base(self, element):
        # Выбрать базу из списка в AxelotStart
        self.driver.find_element(AppiumBy.XPATH,
                        f"//android.widget.TextView[@resource-id='ru.axelot.mobileupdater:id/config_title' and @text={element}]").click()


    def select_task_queue(self,task_queue_group, task_queue):
        # Переход к нужной очереди задач
        self.driver.find_element(AppiumBy.XPATH,
                            f"//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='{task_queue_group}']").click()
        self.driver.find_element(AppiumBy.XPATH,
                            f"//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/action_text' and @text='{task_queue}']").click()

    def select_document(self, element):
        # Выбор документа из списка

        # Добавить скролл до документа

        self.driver.find_element(AppiumBy.XPATH,
                            f"//android.widget.TextView[@resource-id='ru.axelot.wmsx5:id/document_title' and @text='{element}']").click()

    def type_value(self, value):
        # Ввод значения
        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").send_keys(value)
        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
        time.sleep(1)

    def enter_quantity(self, value):
        # Подтверждение количества
        if self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").text == value:
            self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_bottom_panel").click()
        else: raise AssertionError(f'Value {value} are different')
        time.sleep(1)

    def assert_values(self):
        pass



    def finish_check_in_counting(self):
        # Завершить приемку при активной настройке Закрыть поступление при входе - Спросить пользователя

        # добавить проверку на текст по разным операциям  - Завершить приемку, Грузовое место отгружено?
        self.driver.back()
        self.driver.back()
        assert self.driver.find_element(AppiumBy.ID,
                                   "android:id/message").text == 'Завершить приемку ожидаемого поступления? (все товары приняты)'
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()

    def assert_finish_sku_picking(self):
        # Получение всплывающей формы "Получение задач" и выход к списку ОЗ
        assert self.driver.find_element(AppiumBy.ID,"android:id/alertTitle").text == 'Получение задач'
        assert self.driver.find_element(AppiumBy.ID,"android:id/message").text == 'Не найдено задач. Повторить поиск задач?'
        self.driver.find_element(AppiumBy.ID, "android:id/button2").click()
        assert self.driver.find_element(AppiumBy.ID,
                                   "ru.axelot.wmsx5:id/user_name").text == 'Привет, 1!'

    def assert_finish_shipping(self):
        # Завершение отгрузки
        assert self.driver.find_element(AppiumBy.ID,"android:id/alertTitle").text == 'Отгрузка'
        assert self.driver.find_element(AppiumBy.ID,"android:id/message").text == 'Задачи по выбранному документу завершены. Начать работу над новым документом?'
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        assert self.driver.find_element(AppiumBy.ID,
                                   "ru.axelot.wmsx5:id/user_name").text == 'Привет, 1!'

    def finish_task_in_menu(self):
        # Нажать кнопку "Завершить" через Меню
        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/floatingActionButton").click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel").click()

    def finish_receipt_by_lines_with_discrepancies(self):
        # Подтвердить завершение контроля поступления с расхождениями

        self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/button_positive").click()

    def select_value_from_list(self, element):
        # Выбрать элемент из списка через удерживание на поле ввода данных
        clickable = self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel")
        ActionChains(self.driver) \
            .click_and_hold(clickable) \
            .perform()
        self.driver.find_element(AppiumBy.XPATH, f"//android.widget.LinearLayout[@content-desc='{element}']/android.view.ViewGroup").click()


    def long_press(self):

        element = self.driver.find_element(AppiumBy.ID, "ru.axelot.wmsx5:id/editText_bottom_panel")
        action = ActionChains(self.driver)
        click = ActionChains(self.driver)
        action.click_and_hold(element)
        action.perform()
        time.sleep(4)
        action.release(element)
        action.perform()
        time.sleep(0.2)
        action.release(element)

