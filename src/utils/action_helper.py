from datetime import datetime
import random


class ActionHelper:

    def __init__(self, page):
        self.page = page

    def take_validation_screenshot(self):
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_path = f"screenshots/validation/screenshot_{timestamp}.png"
        self.page.screenshot(path=file_path)

    def select_option_from_dropdown(self, option):
        self.page.get_by_role("option", name=option, exact=True).click()

    @staticmethod
    def generate_random_number():
        return random.randint(1, 1000)
