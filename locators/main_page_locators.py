from selenium.webdriver.common.by import By


class MainPageLocators:

    # Вопросы о важном
    FAQ = By.XPATH, ".//div[contains(@class, 'Home_FAQ')]"
    QUESTIONS = By.XPATH, ".//div[@class='accordion__heading']/div[@id='accordion__heading-{}']"
    ANSWERS = By.XPATH, ".//div[@id='accordion__panel-{}']/p"