import pytest
import allure
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from data import Users


class TestOrderPage:
    @allure.title('Проверка заказа самоката')
    @allure.description('Проверка всего флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize("button_order, user_data", [(OrderPageLocators.BUTTON_ORDER_HEAD, Users.user1),
                                                         (OrderPageLocators.BUTTON_ORDER_CONTENT, Users.user2)])
    def test_check_order_positive_two_sets_data(self, driver, button_order, user_data):
        order_page = OrderPage(driver)
        order_page.accept_cookie()
        order_page.scroll_button_order(button_order)
        order_page.wait_button_order(button_order)
        order_page.click_button_order(button_order)
        order_page.fill_form_personal_data(user_data)
        order_page.fill_form_about_rent(user_data)
        assert order_page.check_button_view_order()