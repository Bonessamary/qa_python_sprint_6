from selenium.webdriver.common.by import By


class MainPageLocators:

    # Логотип "Яндекс"
    LOGO_YANDEX = By.XPATH, ".//a[@href='//yandex.ru' and contains(@class, 'Header_LogoYandex')]"

    # Логотип "Самокат"
    LOGO_SCOOTER = By.XPATH, ".//a[@href='/' and contains(@class, 'Header_LogoScooter')]"

    # Заголовок главной страницы
    HEADER_MAIN_PAGE = By.XPATH, ".//div[contains(@class, 'Home_Header')]/[text()='Самокат']"

    # Кнопка согласия с куками
    BUTTON_COOKIE = (By.ID, 'rcc-confirm-button')

    # Кнопка "Статус заказа"
    BUTTON_STATUS_ORDER = By.XPATH, ".//button[text()='Статус заказа']"

    # Вопросы о важном
    FAQ = By.XPATH, ".//div[contains(@class, 'Home_FAQ')]"
    QUESTIONS = By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-{}']"
    ANSWERS = By.XPATH, ".//div[@id='accordion__panel-{}']/p"