import time
from .pages.locators import ProductPageLocators, FixturePageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest


link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_product_page_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
link_main_page = "https://selenium1py.pythonanywhere.com/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_see_product_page(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_page()


def test_guest_see_price(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_see_price()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "ewqrsxdgse3242"
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = link_product_page
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_to_add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_authorized_user()


@pytest.mark.xfail(reason="Because this logic isn't released here yet.")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_on_product_page()


def test_guest_see_message_product_is_added(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_see_message_product_is_added()


@pytest.mark.xfail(reason="Because this logic isn't released here yet.")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = link_product_page_2
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = link_product_page_2
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = link_main_page
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_text_basket_is_empty()


@pytest.mark.need_review
@pytest.mark.parametrize('qparam', ["1","2","3","4","5","6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
#Добавил параметрезацию с пропуском одного параметра (в котором баг)
def test_guest_can_add_product_to_basket(browser, qparam):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{qparam}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_see_message_product_is_added()
    page.should_see_price()
    time.sleep(0)
