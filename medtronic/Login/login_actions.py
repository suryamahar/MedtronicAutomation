
class LoginActions:
    def __init__(self, page):
        self.page = page
        self.username = page.locator(".panel #signInFormUsername")
        self.password = page.locator(".panel #signInFormPassword")
        self.login_btn = page.locator(".panel input[name='signInSubmitButton']")
        self.page_title = page.title()
