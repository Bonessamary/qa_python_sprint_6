import pytest
import allure
from pages.other_page import OtherPage
from locators.order_page_locators import OrderPageLocators
from data import Users


class TestOrderPage:
    @allure.title('Проверка заказа самоката')
    @allure.description('Проверка всего флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize("button_order, user_data", [(OrderPageLocators.BUTTON_ORDER_HEAD, Users.user1),
                                                         (OrderPageLocators.BUTTON_ORDER_CONTENT, Users.user2)])
    def test_check_order_positive_two_sets_data(self, driver, button_order, user_data):
        order_page = OtherPage(driver)
        order_page.accept_cookie()
        order_page.scroll_button_order(button_order)
        order_page.wait_button_order(button_order)
        order_page.click_button_order(button_order)
        order_page.fill_form_personal_data(user_data)
        order_page.fill_form_about_rent(user_data)
        assert order_page.check_button_view_order()

    @allure.title('Проверка перехода на главную страницу Дзена по клику на логотип Яндекса')
    def test_logo_yandex_to_dzen(self, driver):
        main_page = OtherPage(driver)
        main_page.wait_yandex_logo()
        main_page.click_yandex_logo()
        main_page.go_to_next_tab()
        main_page.wait_dzen_url()
        assert main_page.check_current_page_is_dzen()

    @allure.title('Проверка перехода на главную страницу Самоката по клику на логотип Самоката')
    def test_logo_scooter_main_page(self, driver):
        main_page = OtherPage(driver)
        main_page.wait_button_order_head()
        main_page.click_button_order_head()
        main_page.wait_page_order()
        main_page.click_scooter_logo()
        assert main_page.check_current_page_is_main()