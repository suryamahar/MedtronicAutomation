from src.pages.HomePage import HomePage


class LoginPage:
    def __init__(self, page):
        page = page
        self._username = page.locator(".panel #signInFormUsername")
        self._password = page.locator(".panel #signInFormPassword")
        self._login_btn = page.locator(".panel input[name='signInSubmitButton']")
        self._page_title = page.title()

    def enter_username(self, u_name):
        self._username.fill(u_name)

    def enter_password(self, p_word):
        self._password.fill(p_word)

    def click_login(self):
        self._login_btn.click()

    def do_login(self, credentials):
        self.enter_username(credentials.get('username'))
        self.enter_password(credentials.get('password'))
        self.click_login()
        return HomePage
