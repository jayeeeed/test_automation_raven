from playwright.sync_api import Page
from utils.config_loader import load_config


class IntegratedPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_integrations(self):
        config = load_config()
        base_url = config["base_url"]

        self.page.locator("//button[7]").click()
        self.page.wait_for_url(f"{base_url}/integrations/integrated")
        self.page.wait_for_timeout(3000)

    def delete_integrations(self):
        integration_boxes = self.page.locator("//div[2]/div/div[2]/div/div").all()

        for box in integration_boxes:
            if "Salla Livechat" in box.inner_text() or "Jayed" in box.inner_text():
                self._delete_integration(box)
        else:
            assert False, "No integration found"

    def _delete_integration(self, box):
        box.locator("svg.w-5.h-5.-mr-1").click()
        self.page.get_by_role("menuitem", name="Delete").click()
        self.page.get_by_role("button", name="Disconnect").click()
        self.page.locator("svg.ub-w_12px").click()

        box.locator("svg.w-5.h-5.-mr-1").click()
        self.page.get_by_role("menuitem", name="Delete").click()
        self.page.get_by_placeholder("Type 'DELETE' Here").fill("delete")
        self.page.get_by_role("button", name="Delete").click()
        self.page.locator("svg.ub-w_12px").click()
