import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import URLs
from data import QuestionAnswerList


class OtherPage(BasePage):


    @allure.step('Ожидание появления логотипа Яндекса')
    def wait_yandex_logo(self):
        self.waiting_for_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Клик на лого Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Переключение на другую вкладку браузера')
    def go_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидание загрузки страницы Дзен')
    def wait_dzen_url(self):
        self.waiting_for_url(URLs.DZEN_PAGE_URL)

    @allure.step('Ожидание появления кнопки "Заказать" в хедере')
    def wait_button_order_head(self):
        self.waiting_for_element(OrderPageLocators.BUTTON_ORDER_HEAD)

    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_button_order_head(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER_HEAD)

    @allure.step('Ожидание загрузки страницы оформления заказа')
    def wait_page_order(self):
        return self.waiting_for_url(URLs.ORDER_PAGE_URL)

    @allure.step('Ожидание появления логотипа Самоката')
    def wait_scooter_logo(self):
        self.waiting_for_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Клик на логотип Самоката')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Проверка, что текущая страница является главной страницей сайта')
    def check_current_page_is_main(self):
        return self.current_url() == URLs.MAIN_PAGE_URL

    @allure.step('Проверка, что текущая страница является страницей Дзена')
    def check_current_page_is_dzen(self):
        return self.current_url() == URLs.DZEN_PAGE_URL

    @allure.step('Принять куки')
    def accept_cookie(self):
       self.click_on_element(MainPageLocators.BUTTON_COOKIE)

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

    @allure.step('Ожидание появления кнопки Заказать')
    def wait_button_order(self, button):
        self.waiting_for_element(button)

    @allure.step('Скролл до кнопки Заказать')
    def scroll_button_order(self, button):
        self.scroll_to_element(button)

    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order(self, button):
        self.click_on_element(button)

    @allure.step('Заполнение формы "Для кого самокат" + клик на кнопку Дальше')
    def fill_form_personal_data(self, user_data):
        self.waiting_for_element(OrderPageLocators.NAME)
        self.click_on_element(OrderPageLocators.NAME)
        self.text_input_field(OrderPageLocators.NAME, user_data[0])
        self.click_on_element(OrderPageLocators.SURNAME)
        self.text_input_field(OrderPageLocators.SURNAME, user_data[1])
        self.click_on_element(OrderPageLocators.ADDRESS)
        self.text_input_field(OrderPageLocators.ADDRESS, user_data[2])
        self.click_on_element(OrderPageLocators.SUBWAY)
        self.scroll_to_element(OrderPageLocators.LIST_METRO_STATION(user_data[3]))
        self.click_on_element(OrderPageLocators.LIST_METRO_STATION(user_data[3]))
        self.click_on_element(OrderPageLocators.TELEPHONE)
        self.text_input_field(OrderPageLocators.TELEPHONE, user_data[4])
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение формы "Про аренду" + клик на Заказать')
    def fill_form_about_rent(self, user_data):
        self.waiting_for_element(OrderPageLocators.DATE)
        self.click_on_element(OrderPageLocators.DATE)
        self.click_on_element(OrderPageLocators.CHOOSE_DATE(user_data[5]))
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.CHOOSE_PERIOD(user_data[6]))
        self.click_on_element(OrderPageLocators.CHECKBOX_COLOR(user_data[7]))
        self.click_on_element(OrderPageLocators.COMMENT)
        self.text_input_field(OrderPageLocators.COMMENT, user_data[8])
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
        self.waiting_for_element(OrderPageLocators.TITLE_CONFIRM_ORDER)
        self.click_on_element(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)

    @allure.step('Проверка появления кнопки "Посмотреть статус" в окне Заказ оформлен')
    def check_button_view_order(self):
        return self.element_visible(OrderPageLocators.BUTTON_CHECK_STATUS)