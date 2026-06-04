import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption('--browser_name', action="store", default=None,
                    help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action="store", default=True,
                     help="Choose headless option: True or False")


@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless").lower() == "true"
    with sync_playwright() as p:
        print(f"\nstart chrome {browser_name} with headless option = {headless} for test..")
        if browser_name == 'chromium':
            browser = p.chromium.launch(headless=headless)
        else:
            browser = p.firefox.launch(headless=headless)

        context = browser.new_context(
            locale="en-US"
        )

        page = context.new_page()
        yield page
        print(f"\nquit {browser_name} browser..")
        browser.close()
