import allure
import pytest
from pages.button_page import ButtonPage
from pages.order_form import OrderForm
from urls import Urls
from data import user_1, user_2


class TestOrderForm:

    @allure.title('Заполнение формы заказа самоката')
    @allure.description('Заполняем форму заказа самоката, используя две кнопки Заказать как точки входа')
    @pytest.mark.parametrize('name, second_name, address,  phone', [user_1, user_2])
    def test_order_page(self, driver, name, second_name, address, phone):
        order_form = OrderForm(driver)
        order_button = ButtonPage(driver)
        order_form.open(Urls.SCOOTER_URL)
        order_button.order_upper_button_click()
        order_button.order_bottom_button_click()
        order_button_func = getattr(order_form, 'current_url')
        order_button_func()
        order_form.set_name_input(name)
        order_form.set_second_name_input(second_name)
        order_form.set_address_input(address)
        order_form.choose_station()
        order_form.choose_station_click()
        order_form.set_phone_input(phone)
        order_form.continue_button_click()
        order_form.pick_a_date_input()
        order_form.pick_a_duration()
        order_form.color_selection()
        order_form.set_comment_courier()
        order_form.order_confirmation()

        assert order_form.order_confirmed()


