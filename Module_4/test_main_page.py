import pytest
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link_main_page = "http://selenium1py.pythonanywhere.com/"
link_login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = link_main_page
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) # Делаю инициализацию LoginPage
        login_page.should_be_login_page() # Проверяю, что мы на нужной нам странице.

    def test_guest_should_see_login_link(self, browser):
        link = link_main_page
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link() # выполняет метод со страницы main_page (should_be_login_link).


def test_guest_should_see_login_url(browser):
    link = link_login_page
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    link = link_login_page
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    link = link_login_page
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = link_main_page
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_text_basket_is_empty()