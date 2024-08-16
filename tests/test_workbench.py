from medtronic.Homepage.homepage_motherobject import HomepageMotherObject
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from medtronic.Login.login_motherobject import LoginMotherObject

project = HomepageMotherObject.automation_project()
workbench = HomepageMotherObject.automation_workbench()


def test_workbench_creation(login_to_admin, page):
    page = login_to_admin
    login_page = LoginPage(page)
    login_page.do_login(LoginMotherObject.valid_credentials())
    homepage = HomePage(page)
    homepage.create_new_project(project)
    homepage.view_details(project.get('project_title'))
    homepage.create_workbench(workbench)
    homepage.verify_workbench_created(workbench.get('workbench_name'))
