import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, browser, base_url, wait=3):
        self.driver = browser
        self.url = base_url
        self.wait = WebDriverWait(browser, wait)

    @allure.step('Найти элемент {locator} убедиться что он виден')
    def find_element(self, locator='locator'):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Найти элемент {locator} убедиться что он присутствует в DOM')
    def find_invisible_element(self, locator='locator'):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Найти, все элементы {locator}')
    def find_all_elements(self, locator='locator'):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Найти элемент {locator} переместить к нему курсор и сделать клик по нему')
    def click_of_element(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).click().perform()
