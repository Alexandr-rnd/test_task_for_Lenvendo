from selenium.webdriver.common.by import By


class MainPageLocators():
    CARDS_PRISE = (By.CSS_SELECTOR, ".par-options li button")
    CARDS_PRISE_VALUE = (By.CSS_SELECTOR, " .par-options__button--active nobr")
    PLACE_FOR_INPUT_PRICE = (By.CSS_SELECTOR, "input[name=value]")
