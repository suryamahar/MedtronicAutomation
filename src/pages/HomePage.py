from playwright.sync_api import expect
from medtronic.Homepage.homepage_motherobject import HomepageMotherObject
from src.utils.navigation import Navigation
from medtronic.Homepage.hompage_actions import HomepageActions


#This the page class of homepage, all the assertions and methods related to homepage will be avialable here.

class HomePage:
    def __init__(self, page):
        self.page = page
        self._homepage_actions = HomepageActions(self.page)
        self._navigation = Navigation(self.page)

    def verify_title(self, title):
        assert self._homepage_actions.page_title == title

    def verify_valid_login(self):
        self._homepage_actions.medtronic_logo.click()
        expect(self._homepage_actions.medtronic_logo).to_be_visible()
        self._homepage_actions.action_helper.take_validation_screenshot()

    def verify_invalid_login(self):
        expect(self._homepage_actions.incorrect_username_msg).to_be_visible()
        self._homepage_actions.action_helper.take_validation_screenshot()

    def create_new_project(self, project_info):
        self._navigation.navigate_to_homepage()
        self.click_new_project()
        self.fill_project_info(project_info)
        self.click_submit_button()

    def click_new_project(self):
        self._homepage_actions.new_project_btn.click()

    def fill_project_info(self, project_info):
        self._homepage_actions.project_title.fill(project_info.get('project_title'))
        self._homepage_actions.description.fill(project_info.get('description'))
        self._homepage_actions.operating_unit_id.click()
        self._homepage_actions.action_helper.select_option_from_dropdown(project_info.get('operating_unit_id'))
        self._homepage_actions.cost_center.fill(project_info.get('cost_center'))
        self._homepage_actions.data_sets.click()
        self._homepage_actions.action_helper.select_option_from_dropdown(project_info.get('data_sets'))

    def click_submit_button(self):
        self._homepage_actions.submit_btn.click()

    def switch_to_tab(self, tab_name):
        self._homepage_actions.switch_to_tab(tab_name).click()

    def create_workbench(self, workbench_info):
        self.switch_to_tab("Workbench")
        self._homepage_actions.create_workbench_btn.click()
        self._homepage_actions.workbench_name_textbox.fill(workbench_info.get('workbench_name'))
        self._homepage_actions.description_textbox.fill(workbench_info.get('workbench_description'))
        self._homepage_actions.workbench_group_dropdown.click()
        self._homepage_actions.action_helper.select_option_from_dropdown(workbench_info.get('workbench_group'))
        self._homepage_actions.instance_type_dropdown.click()
        self._homepage_actions.action_helper.select_option_from_dropdown(workbench_info.get('instance_type'))
        self._homepage_actions.submit_btn.click()

    def view_details(self, project_title):
        self._homepage_actions.click_view_details_for_project(project_title).click()

    def verify_workbench_created(self, workbench_name: HomepageMotherObject):
        self._homepage_actions.refresh_btn.click()
        expect(self._homepage_actions.workbench_in_workbench_management(workbench_name)).to_be_visible()
        self._homepage_actions.action_helper.take_validation_screenshot()

    def verify_project_exists(self, project_title):
        self._homepage_actions.medtronic_logo.click()
        expect(self._homepage_actions.click_view_details_for_project(project_title)).to_be_visible()
        self._homepage_actions.action_helper.take_validation_screenshot()

    def deactivate_project(self):
        self._homepage_actions.edit_btn.click()
        self._homepage_actions.deactivate_project_btn.click()
        self._homepage_actions.deactivate_i_understand_toggle.click()
        self._homepage_actions.deactivate_btn.click()

    def verify_project_deactivated(self, project_title):
        self._navigation.navigate_to_homepage()
        self._navigation.switch_to_tab("Inactive")
        self.verify_project_exists(project_title)
