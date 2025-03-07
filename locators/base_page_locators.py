from  selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_ORDER_1 = (By.XPATH,
                      "//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']")  # кнопка Заказать вверху страницы
    BUTTON_ORDER_2 = (
    By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # кнопка Заказать внизу страницы
    ACCEPT_COOKIE_BUTTON = (By.XPATH, "//*[contains(@class,'App_CookieButton__3cvqF')]")  # Кнопка  куки все уже привыкли
    YANDEX_LOGO = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')  # логотип яндекс
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")  # логотип самокат




