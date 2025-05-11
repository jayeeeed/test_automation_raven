from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str):
        # self.page.get_by_role("button", name="Continue with Google").click()
        # self.page.get_by_role("textbox", name="Email or phone").fill(email)
        # self.page.get_by_role("textbox", name="Enter your password").fill(password)
        # self.page.get_by_text("Next").click()
        pass

    def change_team(self, team: str):
        self.page.wait_for_timeout(3000)
        self.page.get_by_alt_text("team_avatar").click()
        self.page.locator("#menuModal").get_by_text(team).click()
        self.page.wait_for_timeout(3000)
