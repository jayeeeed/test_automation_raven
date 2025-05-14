import re
from playwright.sync_api import Page, expect


class CreateAgentPage:
    def __init__(self, page: Page):
        self.page = page

    def create_agent(self, name: str, description: str):
        self.page.locator("//div[2]/a/span").click()
        self.page.get_by_role("textbox", name="Name of your agent").fill(name)
        self.page.get_by_role("textbox", name="What your agent will do?").fill(
            description
        )
        self.page.get_by_role("button", name="Save & Continue").click()

    def ticket_tool(self):
        self.page.get_by_role("button", name="Add Action").click()
        self.page.get_by_role("button", name="Assign Ticket").click()
        self.page.get_by_role(
            "textbox", name="When this action will be triggered?"
        ).fill("test tool")
        self.page.get_by_role("combobox", name="Assign to agent or group *").click()
        self.page.get_by_text("Jayed Raven").click()
        self.page.get_by_role("button", name="Save & Continue").click()

    def agent_test(self):
        self.page.get_by_role("button", name="Next").click()

    def deploy_agent(self):
        self.page.locator("//div[1]/button/span").click()
        expect(self.page.locator("//div[1]/button/span")).to_have_attribute(
            "data-state", "checked"
        )
        self.page.get_by_role("button", name="Go to Main Page").click()
        self.page.get_by_role("button", name="Activate Now").click()
