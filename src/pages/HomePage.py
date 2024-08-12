from playwright.sync_api import expect
from src.utils.action_helper import ActionHelper
from medtronic.Homepage.hompage_actions import HomepageActions

#This the page class of homepage, all the assertions and methods related to homepage will be avialable here.

class HomePage:
    def __init__(self,page):
        self.page=page
        self._hompage_actions=HomepageActions(self.page)

    def verify_title(self, title):
        assert self._hompage_actions.page_title==title

    def verify_valid_login(self):
        self._hompage_actions.medtronic_logo.click()
        expect(self._hompage_actions.medtronic_logo).to_be_visible()
        self._hompage_actions.action_helper.take_screenshot()

    def verify_invalid_login(self):
        expect(self._hompage_actions.incorrect_username_msg).to_be_visible() 
        self._hompage_actions.action_helper.take_screenshot()

    def click_new_project(self):
        self._hompage_actions.new_project_btn.click()

    def create_new_project(self):
        self._hompage_actions.click_new_project()
        self._hompage_actions.project_title.fill("Totle")
        self._hompage_actions.description.fill("desc")
        self._hompage_actions.operating_unit_id.click()
        self._hompage_actions.action_helper.select_option_from_dropdown("Cardiovascular_MDT")
        self._hompage_actions.cost_center.fill("cost")
        self._hompage_actions.data_sets.click()
        self._hompage_actions.action_helper.select_option_from_dropdown("Cancer dataset")   
        self._hompage_actions.submit_btn.click()    

    def view_details(self):
        self._hompage_actions.click_view_details_for_project("title").click()

            