from playwright.sync_api import expect
from src.utils.action_helper import ActionHelper

class HomePage:
    def __init__(self,page):
        self.page=page
        self._page_title = page.title()
        self._medtronic_logo = page.locator("img[alt='logo']")
        self._new_project_btn = page.locator("#new-project")
        self._incorrect_username_msg = page.locator(".panel #loginErrorMessage") 
        self._action_helper = ActionHelper(self.page)

    def verify_title(self, title):
        assert self._page_title==title

    def verify_valid_login(self):
        self._medtronic_logo.click()
        expect(self._medtronic_logo).to_be_visible()
        self._action_helper.take_screenshot()

    def verify_invalid_login(self):
        expect(self._incorrect_username_msg).to_be_visible() 
        self._action_helper.take_screenshot()

            
        
