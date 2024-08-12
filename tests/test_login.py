from playwright.async_api import Page,expect
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from medtronic.login_motherobject import LoginMotherObject
from config.config import TestData

def test_valid_login(login_to_admin):
    page=login_to_admin
    loginPage=LoginPage(page)
    loginPage.do_login(LoginMotherObject.valid_credentials())
    hompage=HomePage(page)
    hompage.verify_title(TestData.LOGIN_PAGE_TITLE)
    hompage.verify_valid_login()

def test_invalid_login(login_to_admin):
    page=login_to_admin
    loginPage=LoginPage(page)
    loginPage.do_login(LoginMotherObject.invalid_credentials())
    hompage=HomePage(page)
    hompage.verify_invalid_login()






