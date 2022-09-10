import allure
from src.BasePage import BasePage
from src.MainPageLocators import MainPageLocators
import pytest_check as check


class MainPage(BasePage):

    @allure.step('Открыть главную страницу сайта')
    def open_main_page(self, base_url):
        self.driver.get(base_url)

    @allure.step('Прокликать все карты и проверить активность и соответствие номиналов')
    def activate_all_cards(self):
        cards = self.find_all_elements(MainPageLocators.CARDS_PRISE)
        for i in cards:
            self.click_of_element(i)
            choose_card = self.find_element(MainPageLocators.CARDS_PRISE_VALUE).text
            with allure.step(f'Проверить что кнопка карты с номиналом: {choose_card} активна'):
                check.is_in("par-options__button--active", i.get_attribute("class"), "Выбранная карта не активна")
            price = self.find_invisible_element(MainPageLocators.PLACE_FOR_INPUT_PRICE).get_attribute("value")
            with allure.step(f'Проверить что выбрана карта с номиналом: {choose_card} равна полю "введите": {price}'):
                check.equal(int(choose_card), int(price), "Сумма не соответствует!")
