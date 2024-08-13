from playwright.async_api import Page, expect
from medtronic.Homepage.homepage_motherobject import HomepageMotherObject
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from medtronic.Login.login_motherobject import LoginMotherObject
from config.config import TestData


def test_workbench_creation(login_to_admin):
    page = login_to_admin
    login_page = LoginPage(page)
    login_page.do_login(LoginMotherObject.valid_credentials())
    homepage = HomePage(page)
    homepage.create_new_project(HomepageMotherObject.automation_project())
    homepage.view_details(HomepageMotherObject.automation_project().get('project_title'))
    homepage.create_workbench(HomepageMotherObject.automation_workbench())
    homepage.verify_workbench_created(HomepageMotherObject.automation_workbench().get('workbench_name'))
