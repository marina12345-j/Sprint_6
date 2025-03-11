import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Запрашиваем URL текущей страницы')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Дожидаемся смены URL страницы')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))
        return self.driver.current_url

    @allure.step('Очевидно дожидаемся нужного элемента по локатору')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step('после клика открывается новая вкладка, переключаемся на нее перед проверкой URL')
    def switch_to_new_tab(self):
       WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))  # Ждем открытия новой вкладки
       new_window = self.driver.window_handles[-1]  # Получаем дескриптор новой вкладки
       self.driver.switch_to.window(new_window) # Переключаемся на новую вкладку


    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    @allure.step('Скроллим до элемента по локатору')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step("Открытие страницы заполнения данных заказчика")
    def open(self, url):  # Добавляем параметр url со значением по умолчанию
        self.driver.get(url)  # Открываем переданный URL

