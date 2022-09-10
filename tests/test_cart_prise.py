import allure
from src.MainPage import MainPage


@allure.title("Тест выбора номиналов карт")
def test_cart_prise(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open_main_page(base_url)
    main_page.activate_all_cards()
