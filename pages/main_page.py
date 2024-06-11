import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step('Cкролл до блока с вопросами')
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ)

    @allure.step('Ожидание появления вопроса по запрошенному номеру')
    def wait_question(self, number):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTIONS, number)
        self.waiting_for_element(locator_q_formatted)

    @allure.step('Клик на вопрос')
    def click_question(self, number):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTIONS, number)
        self.click_on_element(locator_q_formatted)

    @allure.step('Ожидание появления ответа')
    def wait_answer(self, number):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWERS, number)
        self.waiting_for_element(locator_a_formatted)

    @allure.step('Получение текста ответа')
    def get_answer_text(self, number):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTIONS, number)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWERS, number)
        self.click_on_element(locator_q_formatted)
        return self.get_text_of_element(locator_a_formatted)