from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str):
        self.page.get_by_role("button", name="Continue with Google").click()
        self.page.get_by_role("textbox", name="Email or phone").fill(email)
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox", name="Enter your password").fill(password)
        self.page.get_by_role("button", name="Next").click()

    def dummy(self):
        pass
