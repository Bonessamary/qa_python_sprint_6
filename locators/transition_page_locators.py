from selenium.webdriver.common.by import By


class TransitionPageLocators:

    # Логотип "Яндекс"
    LOGO_YANDEX = By.XPATH, ".//a[@href='//yandex.ru' and contains(@class, 'Header_LogoYandex')]"

    # Логотип "Самокат"
    LOGO_SCOOTER = By.XPATH, ".//a[@href='/' and contains(@class, 'Header_LogoScooter')]"

    # Кнопка "Заказать" вверху
    BUTTON_ORDER_HEAD = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")