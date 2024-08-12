import pytest

@pytest.fixture
def login_to_admin(page):
    page.goto("https://dqzgfcurugtza.cloudfront.net/?code=380e02bf-556a-484d-93e0-aa35eb7e2eb2")
    page.click("//a[text()='here']")
    yield page