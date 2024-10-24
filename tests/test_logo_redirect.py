import allure
import pytest
from conftest import driver
from page_objects.main_page import MainPage

class TestLogoRedirect:
    @allure.title('Проверка: нажатие на логотип "Самоката" ведет на главную страницу')
    @allure.step('Тестирование клика по логотипу "Самоката"')
    def test_redirect_to_main_page_via_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_scooter_logo_in_header()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка: нажатие на логотип Яндекса открывает главную страницу Дзена в новом окне')
    @allure.step('Тестирование клика по логотипу Яндекса')
    def test_redirect_to_dzen_via_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_yandex_order_button_in_header_to_be_visible()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert 'Дзен' in main_page.get_page_title()