class Navigation:
    def __init__(self, page):
        self.page = page

    def navigate_to_homepage(self):
        self.page.locator("div[id='Project Dashboard_button_0']").click()

    def switch_to_tab(self, tab):
        self.page.get_by_role("tab", name=tab).click()
