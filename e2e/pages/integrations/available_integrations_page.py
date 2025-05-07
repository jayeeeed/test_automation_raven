from playwright.sync_api import Page
from utils.config_loader import load_config


class IntegrationsPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_integrations(self):
        config = load_config()
        base_url = config["base_url"]

        self.page.locator("//button[7]").click()
        self.page.wait_for_url(f"{base_url}/integrations/integrated")

        self.page.wait_for_timeout(1000)
        self.page.locator("//span[contains(text(), 'Available Integrations')]").click()
        self.page.wait_for_url(f"{base_url}/integrations/available-integrations")

    def goto_woocommerce_shopify_zid(self, integration, url):
        self.page.get_by_role("heading", name=f"{integration}").click()
        self.page.get_by_role("button", name="Continue").click()

        new_tab = self.page.context.wait_for_event("page")
        new_tab.wait_for_load_state("domcontentloaded")
        assert url in new_tab.url
        new_tab.close()
        self.page.locator("svg.cursor-pointer").click()

    def goto_salla(self):
        self.page.get_by_role("heading", name="Salla").click()
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Complete").click()

    def goto_meta(self, integration, url):
        self.page.get_by_role("heading", name=f"{integration}").click()

        if integration == "WhatsApp":
            self.page.get_by_role("button", name="Connect Whatsapp").click()
        else:
            self.page.get_by_role("button", name="Next").click()
            self.page.wait_for_timeout(500)
            self.page.get_by_role("button", name="Login with Personal Account").click()

        child_page = self.page.context.wait_for_event("page")
        child_page.wait_for_load_state("domcontentloaded")
        assert url in child_page.url
        child_page.close()
        self.page.locator("[data-testid='icon-id-1']").click()

    def go_to_email(self):
        self.page.get_by_role("heading", name="Email").click()
        self.page.locator("svg.cursor-pointer").click()

    def go_to_viber_telegram_line(self, integration):
        self.page.get_by_role("heading", name=f"{integration}").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.locator("[data-testid='icon-id-1']").click()

    def go_to_live_chat_plugin(self):
        self.page.get_by_role("heading", name="Live Chat Plugin").click()
        self.page.get_by_role("button", name="Confirm Integration").click()
        self.page.get_by_role("button", name="Finish").click()
