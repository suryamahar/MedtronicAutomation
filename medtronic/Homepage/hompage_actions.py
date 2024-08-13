from src.utils.action_helper import ActionHelper


class HomepageActions:
    def __init__(self, page):
        self.page = page
        self.page_title = page.title()
        self.medtronic_logo = page.locator("img[alt='logo']")
        self.new_project_btn = page.get_by_role("button", name="New Project")
        self.incorrect_username_msg = page.locator(".panel #loginErrorMessage")
        self.project_title = page.locator("#outlined-static-input").first
        self.description = page.locator("#outlined-static-text-area")
        self.operating_unit_id = page.locator("//div[text()='Operating Unit ID']/../following-sibling::div//input")
        self.cost_center = page.locator("//div[text()='Cost Center']/../following-sibling::div//input")
        self.data_sets = page.locator("//div[text()='Datasets']/../following-sibling::div//input")
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.create_workbench_btn = page.get_by_role("button", name="Create Workbench")
        self.workbench_name_textbox = page.locator("//div[text()='Workbench Name']/../following-sibling::div//input")
        self.description_textbox = page.locator("//div[text()='Description']/../following-sibling::div//input")
        self.workbench_group_dropdown = page.locator("//div[text()='Workbench Group']/../following-sibling::div//input")
        self.instance_type_dropdown = page.locator("//div[text()='Instance Type']/../following-sibling::div//input")
        self.refresh_btn = page.get_by_role("button", name="Refresh")
        self.action_helper = ActionHelper(self.page)

    def click_view_details_for_project(self, project):
        return self.page.locator(f"//div[h4[text()='{project}']]/..//button")

    def switch_to_tab(self, tab):
        return self.page.get_by_role("tab", name=tab)

    def workbench_in_workbench_management(self, workbench):
        return self.page.locator(f"//div[contains(@class,'MuiGrid-grid-xs-3')]//p[text()='{workbench}']")
