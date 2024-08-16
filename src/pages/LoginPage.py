from src.pages.HomePage import HomePage
from medtronic.Login.login_actions import LoginActions


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._login_actions = LoginActions(self.page)

    def enter_username(self, u_name):
        self._login_actions.username.fill(u_name)

    def enter_password(self, p_word):
        self._login_actions.password.fill(p_word)

    def click_login(self):
        self._login_actions.login_btn.click()

    def do_login(self, credentials):
        self.enter_username(credentials.get('username'))
        self.enter_password(credentials.get('password'))
        self.click_login()
        return HomePage
