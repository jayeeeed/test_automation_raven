import re
from playwright.sync_api import Page, expect
from utils.config_loader import load_config


class WorkflowDashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_workflow(self):
        config = load_config()
        base_url = config["base_url"]

        self.page.locator("//button[6]").click()
        self.page.wait_for_url(f"{base_url}/projects/**/workflow-automation")
        self.page.wait_for_timeout(3000)

    def verify_workflow(self, workflow_name):
        self.page.wait_for_timeout(3000)
        expect(self.page.locator("//table/tbody/tr[1]/td[1]").first).to_have_text(
            workflow_name
        )

    def edit_workflow(self, workflow_name):
        self.page.get_by_text(workflow_name).hover()
        self.page.locator("//div[5]/div/div[2]/div[2]").click()
        self.page.get_by_role("menuitem", name="Edit").click()
