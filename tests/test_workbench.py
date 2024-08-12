from playwright.async_api import Page,expect
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from medtronic.Login.login_motherobject import LoginMotherObject
from config.config import TestData

def test_workbench_creation(login_to_admin):
    page=login_to_admin
    loginPage=LoginPage(page)
    loginPage.do_login(LoginMotherObject.valid_credentials())
    homepage=HomePage(page)
   # homepage.create_new_project()
    homepage.view_details()