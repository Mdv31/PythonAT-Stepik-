from selenium.webdriver.common.by import By


#class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_LOGIN = (By.XPATH, "//*[@id=\"messages\"]/div")
    ERROR_MESSAGE = (By.XPATH, "//*[@id=\"register_form\"]/div[1]")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRICE = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/p[1]")
    BASKET_PRICE = (By.XPATH, "// *[@id =\"messages\"]/div[3]/div/p[1]/strong")
    PRODUCT = (By.XPATH, "//strong[text()=\"The shellcoder's handbook\"]")
    MESSAGE_PRODUCT = (By.XPATH, "//*[@id=\"messages\"]/div[1]/div/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]/div[1]/div")
    PRODUCT = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Добавили кортеж из двух значений.
    BASKET_BUTTON = (By.XPATH, "//*[@id=\"default\"]/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div.content")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset > div:nth-child(n)")


class FixturePageLocators():
    EMAIL = (By.XPATH, "//*[@id=\"id_registration-email\"]")
    PASSWORD1 = (By.XPATH, "//*[@id=\"id_registration-password1\"]")
    PASSWORD2 = (By.XPATH, "//*[@id=\"id_registration-password2\"]")
    BUTTON = (By.XPATH, "//*[@id=\"register_form\"]/button")