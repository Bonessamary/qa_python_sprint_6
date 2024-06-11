import allure
from pages.base_page import BasePage
from locators.transition_page_locators import TransitionPageLocators
from data import URLs


class TransitionPage(BasePage):

    @allure.step('Ожидание появления логотипа Яндекса')
    def wait_yandex_logo(self):
        self.waiting_for_element(TransitionPageLocators.LOGO_YANDEX)

    @allure.step('Клик на лого Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(TransitionPageLocators.LOGO_YANDEX)

    @allure.step('Переключение на другую вкладку браузера')
    def go_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидание загрузки страницы Дзен')
    def wait_dzen_url(self):
        self.waiting_for_url(URLs.DZEN_PAGE_URL)

    @allure.step('Проверка, что текущая страница является страницей Дзена')
    def check_current_page_is_dzen(self):
        return self.current_url() == URLs.DZEN_PAGE_URL

    @allure.step('Ожидание появления кнопки "Заказать" в хедере')
    def wait_button_order_head(self):
        self.waiting_for_element(TransitionPageLocators.BUTTON_ORDER_HEAD)

    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_button_order_head(self):
        self.click_on_element(TransitionPageLocators.BUTTON_ORDER_HEAD)

    @allure.step('Ожидание загрузки страницы оформления заказа')
    def wait_page_order(self):
        return self.waiting_for_url(URLs.ORDER_PAGE_URL)

    @allure.step('Клик на логотип Самоката')
    def click_scooter_logo(self):
        self.click_on_element(TransitionPageLocators.LOGO_SCOOTER)

    @allure.step('Проверка, что текущая страница является главной страницей сайта')
    def check_current_page_is_main(self):
        return self.current_url() == URLs.MAIN_PAGE_URL