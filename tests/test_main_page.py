import pytest
import allure
from pages.main_page import MainPage
from data import QuestionAnswerList


class TestMainPage:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка, что вопросу соответствует правильный ответ')
    @pytest.mark.parametrize("number, expected_result", QuestionAnswerList.question_answer_set)
    def test_faq_on_main_page(self, driver, number, expected_result):
        main_page = MainPage(driver)
        main_page.scroll_to_faq()
        main_page.wait_question(number)
        main_page.click_question(number)
        main_page.wait_answer(number)
        assert main_page.get_answer_text(number) == expected_result, 'Не получен ожидаемый ответ на вопрос'