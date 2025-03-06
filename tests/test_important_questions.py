import allure
import pytest
from conftest import driver
from urls import Urls
from pages.button_page import ButtonPage
from data import answers


class TestHomePageQuestions:

    @allure.title('Проверка раздела Вопросы о важном')
    @allure.description('Проверка появления соответствующего текста ответа при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question', answers)
    def test_click_and_get_answer(self, driver, question):
        number, question = question
        button_page = ButtonPage(driver)
        button_page.cookie_click()
        button_page.scroll_to_element()
        button_page.wait_for_element_appears()
        button_page.click_and_get_answer(number)
        assert button_page.click_and_get_answer(number).text == question


    @allure.title('Проверка перехода на страницу Дзена после нажатия на лого Яндекса')
    @allure.description('Нажимаем на лого Яндекса и проверяем, что новое окно — Яндекс Дзен')
    def test_transition_yandex(self, driver):
        button_page = ButtonPage(driver)
        button_page.cookie_click()
        button_page.yandex_logo_button_click()
        expected_url = "https://dzen.ru/?yredirect=true"
        button_page.wait_url_changes(expected_url)
        assert expected_url == Urls.DZEN_URL

    @allure.title('Проверка нажатия на логотип "Самокат"')
    @allure.description('Проверка перехода на главную страницу при нажатии на логотип "Самокат"')
    def test_click_logo_samokat_open_home_page(self, driver):
        button_page = ButtonPage(driver)
        button_page.order_upper_button_click()
        button_page.scooter_logo_button_click()
        assert driver.current_url == Urls.SCOOTER_URL