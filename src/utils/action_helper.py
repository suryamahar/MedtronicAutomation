from datetime import datetime
class ActionHelper():

    def __init__(self,page):
        self.page=page

    def take_screenshot(self):
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_path = f"screenshot/screenshot_{timestamp}.png"
        self.page.screenshot(path=file_path)