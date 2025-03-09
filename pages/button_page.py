from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from locators.buttons_questions_click import ButtonsClick
from pages.base_page import BasePage
import allure
from urls import Urls

@allure.step('Вытаскиваем по номеру и возвращаем локаторы вопросов')
def question_locator(number):
    return ButtonsClick.QUESTIONS[number]

@allure.step('Вытаскиваем по номеру и возвращаем локаторы ответов')
def answer_locator(number):
    return ButtonsClick.ANSWERS[number]

class ButtonPage(BasePage):


  #  @allure.step('Переключаемся на новое окно')
   # def switch_driver_dzen(self):
    #    original_url = self.driver.current_url
      #  WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(original_url))    # Ожидаем изменения URL
       # original_window = self.driver.current_window_handle
        #WebDriverWait(self.driver, 10).until(expected_conditions.new_window_is_opened(original_window))
        #new_window = [window for window in self.driver.window_handles if window != original_window][0]
        #self.driver.switch_to.window(new_window)

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_url_changes(Urls.DZEN_URL)

    @allure.step('Нажимаем на кнопку  Куки все уже привыкли')
    def cookie_click(self):
        self.click(BasePageLocators.ACCEPT_COOKIE_BUTTON)

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
        self.click(BasePageLocators.BUTTON_ORDER_1)

    @allure.step('Нажимаем на кнопку Заказа внизу страницы')
    def order_bottom_button_click(self):
        self.click(BasePageLocators.BUTTON_ORDER_2)

    @allure.step('Нажимаем на кнопку сервиса Самокат вверху страницы')
    def scooter_logo_button_click(self):
        self.click(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Нажимаем на кнопку Яндекса вверху страницы')
    def yandex_logo_button_click(self):
        self.click(BasePageLocators.YANDEX_LOGO)


        #print("Ожидаем появления кнопки Яндекса...")
        #WebDriverWait(self.driver, 10).until(
         #   expected_conditions.element_to_be_clickable(BasePageLocators.YANDEX_LOGO)
        #)
        #print("Кнопка Яндекса доступна, нажимаем...")
        #self.click(BasePageLocators.YANDEX_LOGO)
        #time.sleep(3)  # Временное ожидание
        #current_url = self.driver.current_url
        #print(f"Текущий URL: {current_url}")
        #self.click(BasePageLocators.YANDEX_LOGO)



