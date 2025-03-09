import allure
from locators.name_address import NameAddress
from pages.base_page import BasePage
from urls import Urls

class OrderForm(BasePage):



    @allure.step('Заполняем поле Имя')
    def set_name_input(self, name):
        name_input = self.wait_and_find_element(NameAddress.FIELD_NAME)
        name_input.send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_second_name_input(self, second_name):
        second_name_input = self.wait_and_find_element(NameAddress.FIELD_LAST_NAME)
        second_name_input.send_keys(second_name)

    @allure.step('Заполняем поле Адрес')
    def set_address_input(self, address):
        address_input = self.wait_and_find_element(NameAddress.FIELD_ADDRESS)
        address_input.send_keys(address)

    @allure.step('Заполняем станцию метро')
    def choose_station(self,):
        station_input = self.wait_and_find_element(NameAddress.METRO_STATION)
        station_input.click()

    @allure.step('Выбираем станцию метро')
    def choose_station_click(self):
        station_input_click = self.wait_and_find_element(NameAddress.SELECTED_STATION)
        station_input_click.click()

    @allure.step('Заполняем поле Номер')
    def set_phone_input(self, phone):
        phone_input = self.wait_and_find_element(NameAddress.FIELD_TELEPHONE)
        phone_input.send_keys(phone)

    @allure.step('Нажать кнопку Далее')
    def continue_button_click(self):
        self.wait_and_find_element(NameAddress.BUTTON_FURTHER).click()

    @allure.step('Заполняем поле выбора даты')
    def pick_a_date_input(self):
        self.wait_and_find_element(NameAddress.DATE_PICKER_INPUT_FIELD).click()
        self.wait_and_find_element(NameAddress.DATE_PICKER_CHOOSE_DATE).click()

    @allure.step('Заполняем поле срока аренды')
    def pick_a_duration(self):
        self.wait_and_find_element(NameAddress.FIELD_RENTAL_PERIOD).click()
        self.wait_and_find_element(NameAddress.DROPDOWN_ITEM_RENTAL_PERIOD).click()

    @allure.step('Выбираем цвет самоката черный')
    def color_selection(self):
        self.wait_and_find_element(NameAddress.FIELD_COLOR_SCOOTER_BLACK).click()

    @allure.step('Комментарий для курьера')
    def set_comment_courier(self, comment = 'Ждем'):
        comment_courier = self.wait_and_find_element(NameAddress.FIELD_COMMIT)
        comment_courier.send_keys(comment)

    @allure.step('Подтверждаем заказ - нажимаем заказать и да')
    def order_confirmation(self):
        self.wait_and_find_element(NameAddress.BUTTON_ORDER).click()
        self.wait_and_find_element(NameAddress.BUTTON_OK).click()

    @allure.step('Находим текст в окне с подтвержденным заказом')
    def order_confirmed(self):
        self.wait_and_find_element(NameAddress.HEADING_ORDER_PLACED)
        return True


