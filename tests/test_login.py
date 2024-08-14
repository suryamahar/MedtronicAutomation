from playwright.async_api import Page, expect
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from medtronic.Login.login_motherobject import LoginMotherObject
from config.config import TestData


def test_valid_login(login_to_admin, page):
    page = login_to_admin
    login_page = LoginPage(page)
    login_page.do_login(LoginMotherObject.valid_credentials())
    homepage = HomePage(page)
    homepage.verify_title(TestData.LOGIN_PAGE_TITLE)
    homepage.verify_valid_login()


def test_invalid_login(login_to_admin, page):
    page = login_to_admin
    login_page = LoginPage(page)
    login_page.do_login(LoginMotherObject.invalid_credentials())
    homepage = HomePage(page)
    homepage.verify_invalid_login()
