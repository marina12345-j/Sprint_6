from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class NameAddress(BasePageLocators):



    FIELD_NAME = (By.XPATH, "//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Имя']") #  поле Имя
    FIELD_LAST_NAME = (By.XPATH, "//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Фамилия']") # поле Фамилия
    FIELD_ADDRESS = (By.XPATH, "//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Адрес: куда привезти заказ']") # поле Адрес
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")# Поле Станция метро
    SELECTED_STATION = (By.XPATH, "//div[text()='Черкизовская']") # Выбранная станция метро
    FIELD_TELEPHONE = (By.XPATH, "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Телефон: на него позвонит курьер']") # поле Телефон
    BUTTON_FURTHER = (By.XPATH, "//button [@class='Button_Button__ra12g Button_Middle__1CSJM']")# кнопка Далее

# Поле про аренду
    HEADING_ABOUT_RENT = (By.XPATH, "//div[@class='Order_Header__BZXOb']") # заголовок Про аренду
    FIELD_DATA = (By.XPATH, "//input[@class= 'Input_Input__1iN_Z Input_Responsible__1jDKN']/input[@placeholder='Когда привезти самокат']") # поле когда привезти самокат
    DATE_PICKER_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_CHOOSE_DATE = (By.XPATH, "//div[@aria-label='Choose среда, 5-е марта 2025 г.']")

    TOMORROW_DATE_CALENDAR = (By.XPATH, "following-sibling::div[1]") # Завтрашняя дата в календаре
    FIELD_RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']") # поле Срок аренды
    RENTAL_DURATION_LIST = (By.CLASS_NAME, 'Dropdown-menu')# Выпадающий список с количеством дней аренды
    DROPDOWN_ITEM_RENTAL_PERIOD = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']") # Трое суток
    FIELD_COLOR_SCOOTER_BLACK = (By.XPATH, "//*[@id='black']") # поле Цвет самоката чек-бокс черный
    FIELD_COLOR_SCOOTER_GREY = (By.XPATH, "//*[@id='grey']") # поле Цвет самоката чек-бокс серый
    FIELD_COMMIT = (By.XPATH, "//input[@class= 'Input_Input__1iN_Z Input_Responsible__1jDKN']") # поле Комментарий для курьера
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") # Кнопка Заказать
    BUTTON_BACK = (By.XPATH, "//button[text()='Назад']") # кнопка Назад
    BUTTON_ORDER_1 = (By.XPATH,"//div[@class='Order_Buttons__1xGrp']")  # кнопка Далее

# Хотите оформить заказ?
    BUTTON_OK = (By.XPATH, "//button[text()='Да']") # кнопка Да
    HEADING_ORDER_PLACED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']") # сообщение Заказ оформлен