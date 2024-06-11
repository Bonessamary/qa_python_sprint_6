from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание загрузки элемента')
    def waiting_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание загрузки страницы')
    def waiting_for_url(self, url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Проверка видимости элемента')
    def element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ввести текст в поле')
    def text_input_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Форматирование локатора')
    def format_locators(self, locator_1, number):
        method, locator = locator_1
        locator = locator.format(number)
        return (method, locator)