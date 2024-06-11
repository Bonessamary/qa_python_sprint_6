from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Кнопка согласия с куками
    BUTTON_COOKIE = (By.ID, 'rcc-confirm-button')

    # Кнопка "Заказать" вверху
    BUTTON_ORDER_HEAD = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")

    # Кнопка "Заказать" внизу
    BUTTON_ORDER_CONTENT = By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"

    # Раздел "Для кого самокат"

    # Поле "Имя"
    NAME = By.XPATH, ".//input[@placeholder='* Имя']"

    # Поле "Фамилия"
    SURNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"

    # Поле "Адрес: куда привезти самокат"
    ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"

    # Поле "Станция метро"
    SUBWAY = By.XPATH, ".//input[@placeholder='* Станция метро']"

    # Метод, который возвращает станцию метро
    @staticmethod
    def LIST_METRO_STATION(data=''):
        return [By.XPATH, f'//li[@data-value="{data}"]']

    # Поле "Телефон: на него позвонит курьер"
    TELEPHONE = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"

    # Кнопка "Далее" на странице заказа
    BUTTON_NEXT = By.XPATH, ".//button[text()='Далее']"

    # Раздел "Про аренду"

    # Поле "Когда привезти самокат"
    DATE = By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']"

    # Метод который возвращает дату
    @staticmethod
    def CHOOSE_DATE(data=0):
        return By.CSS_SELECTOR, f".react-datepicker__day--{data}"

    # Поле "Срок аренды"
    RENTAL_PERIOD = By.XPATH, ".//div[text()='* Срок аренды']"

    # Выбрать количество период аренды
    @staticmethod
    def CHOOSE_PERIOD(data=''):
        return By.XPATH, f".//div[@class='Dropdown-option' and text()='{data}']"

    # Выбор цвета самоката
    @staticmethod
    def CHECKBOX_COLOR(data=''):
        return By.XPATH, f".//input[@id='{data}']"

    # Поле "Комментарий для курьера"
    COMMENT = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"

    # Кнопка "Заказать" на странице заказа
    BUTTON_ORDER = By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"

    # Заголовок окна подтверждения заказа
    TITLE_CONFIRM_ORDER = By.XPATH, ".//div[text()='Хотите оформить заказ?']"

    # Кнопка "Да" окна "Хотите оформить заказ?"
    BUTTON_YES_CONFIRM_ORDER = By.XPATH, ".//button[text()='Да']"

    # Кнопка "Посмотреть статус" в окне "Заказ оформлен"
    BUTTON_CHECK_STATUS = By.XPATH, ".//button[text()='Посмотреть статус']"