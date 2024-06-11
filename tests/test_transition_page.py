import allure
from pages.transition_page import TransitionPage

class TestTransitionPage:

    @allure.title('Проверка перехода на главную страницу Дзена по клику на логотип Яндекса')
    def test_logo_yandex_to_dzen(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.wait_yandex_logo()
        transition_page.click_yandex_logo()
        transition_page.go_to_next_tab()
        transition_page.wait_dzen_url()
        assert transition_page.check_current_page_is_dzen()

    @allure.title('Проверка перехода на главную страницу Самоката по клику на логотип Самоката')
    def test_logo_scooter_main_page(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.wait_button_order_head()
        transition_page.click_button_order_head()
        transition_page.wait_page_order()
        transition_page.click_scooter_logo()
        assert transition_page.check_current_page_is_main()