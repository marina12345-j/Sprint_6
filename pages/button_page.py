from locators.buttons_questions_click import ButtonsClick
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from urls import Urls

@allure.step('Вытаскиваем по номеру и возвращаем локаторы вопросов')
def question_locator(number):
    return ButtonsClick.QUESTIONS[number]


@allure.step('Вытаскиваем по номеру и возвращаем локаторы ответов')
def answer_locator(number):
    return ButtonsClick.ANSWERS[number]

class ButtonPage(BasePage):

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_is('Дзен')

    @allure.step('Ищем вопросы, раскрываем их и фиксируем ответы')
    def click_and_get_answer(self, number):
        self.wait_and_find_element(question_locator(number)).click()
        return self.wait_and_find_element(answer_locator(number))

    @allure.step('Скроллим до нужного элемента')
    def scroll_to_element(self):
        self.scroll(ButtonsClick.QUESTIONS[1])

    @allure.step('Ожидаем появления элемента, до которого скроллили')
    def wait_for_element_appears(self):
        self.wait_and_find_element(ButtonsClick.QUESTIONS[1])

    @allure.step('Нажимаем на кнопку Заказа вверху страницы')
    def order_upper_button_click(self):
        self.click(ButtonsClick.BUTTON_ORDER_1)

    @allure.step('Нажимаем на кнопку Заказа внизу страницы')
    def order_bottom_button_click(self):
        self.click(ButtonsClick.BUTTON_ORDER_2)

    @allure.step('Нажимаем на кнопку сервиса Самокат вверху страницы')
    def scooter_logo_button_click(self):
        self.click(ButtonsClick.SCOOTER_LOGO)

    @allure.step('Нажимаем на кнопку Яндекса вверху страницы')
    def yandex_logo_button_click(self):
        self.click(ButtonsClick.YANDEX_LOGO)



