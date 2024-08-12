from src.utils.action_helper import ActionHelper

class HomepageActions:
    def __init__(self,page):
        self.page=page
        self.page_title = page.title()
        self.medtronic_logo = page.locator("img[alt='logo']")
        self.new_project_btn = page.get_by_role("button", name="New Project")
        self.incorrect_username_msg = page.locator(".panel #loginErrorMessage") 
        self.project_title = page.locator("#outlined-static-input").first
        self.description = page.locator("#outlined-static-text-area")
        self.operating_unit_id = page.locator("//div[text()='Operating Unit ID']/../following-sibling::div//input")
        self.cost_center = page.locator("//div[text()='Operating Unit ID']/../following-sibling::div//input")
        self.data_sets = page.locator("//div[text()='Datasets']/../following-sibling::div//input")
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.action_helper = ActionHelper(self.page)

    def click_view_details_for_project(self,project):
        return self.page.locator(f"//div[h4[text()='{project}'] and //button[text()='View Details']]")
        