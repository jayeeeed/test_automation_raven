import allure
import pytest
from tests.base_test import login
from pages.integrations.available_integrations_page import IntegrationsPage
from utils.config_loader import load_config


@pytest.mark.skip(reason="Skipping this test for now")
@allure.feature("Integrations Functionality")
@allure.story("User integrates with stores")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://your_project_tracking_url", name="Project Tracking Link")
@allure.description("This test verifies that the user can integrate with stores.")
def test_integrations(browser_context):
    page = browser_context

    with allure.step("Log in to the application"):
        login(page)

    with allure.step("Load configuration and navigate to integrations"):
        config = load_config()
        meta_url = config["meta_url"]
        woocommerce_url = config["woocommerce_url"]
        shopify_url = config["shopify_url"]
        zid_url = config["zid_url"]

        integrations_page = IntegrationsPage(page)
        integrations_page.goto_integrations()

    with allure.step("Verify E-COMMERCE integrations"):
        integrations = {
            "WooCommerce": woocommerce_url,
            "Shopify": shopify_url,
            "Zid": zid_url,
        }
        for integration, url in integrations.items():
            with allure.step(f"Verify {integration} integration"):
                integrations_page.goto_woocommerce_shopify_zid(integration, url)

        with allure.step("Verify Salla integrations"):
            integrations_page.goto_salla()

    with allure.step("Verify CHANNEL integrations"):
        integrations = {
            "Facebook Feed": meta_url,
            "Messenger": meta_url,
            "Instagram Feed": meta_url,
            "Instagram Chat": meta_url,
            "WhatsApp": meta_url,
        }
        for integration, url in integrations.items():
            with allure.step(f"Verify {integration} integration"):
                integrations_page.goto_meta(integration, url)

    with allure.step("Verify Channel integrations"):
        with allure.step("Verify email integrations"):
            integrations_page.go_to_email()

        integrations = [
            "Viber",
            "Telegram",
            "Line",
        ]

        for integration in integrations:
            with allure.step(f"Verify {integration} integration"):
                integrations_page.go_to_viber_telegram_line(integration)

        with allure.step("Verify live chat plugin integrations"):
            integrations_page.go_to_live_chat_plugin()

    allure.attach(
        page.screenshot(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
