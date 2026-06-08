from .base_page import BasePage
from playwright.sync_api import expect


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.page.locator("#login_link")
        login_link.click()

    def should_be_login_link(self):
        expect(self.page.locator("#login_link_invalid")).to_be_visible()
