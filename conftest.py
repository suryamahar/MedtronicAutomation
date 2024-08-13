import time

import pytest
from playwright.sync_api import sync_playwright
from config.config import TestData


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.set_default_timeout(100000)
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()


@pytest.fixture
def login_to_admin(page):
    page.goto(TestData.BASE_STAGE_URL)
    time.sleep(5)
    count = page.locator("//a[text()='here']").count()
    if count > 0:
        page.locator("//a[text()='here']").click()
    yield page
