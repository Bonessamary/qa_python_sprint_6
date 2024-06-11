import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Принять куки')
    def accept_cookie(self):
       self.click_on_element(OrderPageLocators.BUTTON_COOKIE)

    @allure.step('Скролл до кнопки Заказать')
    def scroll_button_order(self, button):
        self.scroll_to_element(button)

    @allure.step('Ожидание появления кнопки Заказать')
    def wait_button_order(self, button):
        self.waiting_for_element(button)

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