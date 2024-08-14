from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from medtronic.Login.login_motherobject import LoginMotherObject
from medtronic.Homepage.homepage_motherobject import HomepageMotherObject


def test_project_creation(login_to_admin, page):
    page = login_to_admin
    login_page = LoginPage(page)
    login_page.do_login(LoginMotherObject.valid_credentials())
    homepage = HomePage(page)
    homepage.create_new_project(HomepageMotherObject.automation_project())
    homepage.verify_project_exists(HomepageMotherObject.automation_project().get('project_title'))


def test_deactivate_project(login_to_admin, page):
    page = login_to_admin
    login_page = LoginPage(page)
    login_page.do_login(LoginMotherObject.valid_credentials())
    homepage = HomePage(page)
    homepage.view_details(HomepageMotherObject.automation_project().get('project_title'))
    homepage.deactivate_project()
    homepage.verify_project_deactivated(HomepageMotherObject.automation_project().get('project_title'))
