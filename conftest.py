import pytest
import os


@pytest.fixture
def login_to_admin(page):
    page.goto("https://dqzgfcurugtza.cloudfront.net/?code=380e02bf-556a-484d-93e0-aa35eb7e2eb2")
    page.click("//a[text()='here']")
    yield page


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        report = item.config.pluginmanager.getplugin('terminalreporter').reporter
        # Capture the screenshot if the test fails
        page = item.funcargs.get('browser')
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            page.screenshot(path=screenshot_path)
            report.write(f"\nScreenshot saved to: {screenshot_path}\n")
