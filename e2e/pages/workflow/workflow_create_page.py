import re
from playwright.sync_api import Page, expect
from utils.config_loader import load_config


class WorkflowCreatePage:
    def __init__(self, page: Page):
        self.page = page

    def create_workflow(self, workflow_name: str):
        self.page.get_by_role("button", name="Create Automation").click()
        self.page.locator("//main/div/div/div/div/div[1]/div[1]/button[2]").click()
        self.page.get_by_role("textbox").fill(workflow_name)

        self.page.locator("[data-testid='rf__node-node-0']").click()
        self.page.get_by_role("heading", name="Order Created").click()
        self.page.get_by_role("button", name="Save Trigger").click()

        ##################### Condition start #####################
        self.page.get_by_text("Condition", exact=True).click()
        self.page.get_by_role("button", name="Add New Condition").click()
        self.page.get_by_role("heading", name="Attribute").click()

        ##################### Attributes #####################
        # Billing Phone Number
        self.page.get_by_role("heading", name="Billing Phone Number").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="starts with").click()
        self.page.get_by_role("textbox", name="Value").first.fill("+880")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Customer Phone Number
        self.page.get_by_role("heading", name="Customer Phone Number").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="starts with").click()
        self.page.get_by_role("textbox", name="Value").nth(1).fill("+880")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Default Phone Number
        self.page.get_by_role("heading", name="Default Phone Number").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="starts with").click()
        self.page.get_by_role("textbox", name="Value").nth(2).fill("+880")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Generated Discount Code
        self.page.get_by_role("heading", name="Generated Discount Code").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="exists", exact=True).click()
        self.page.get_by_role("textbox", name="Value").nth(3).fill("Y")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Order Created Date
        self.page.get_by_role("heading", name="Order Created Date").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is greater or equal to").click()
        self.page.get_by_role("textbox", name="Value").nth(4).fill("2025-02-01")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Order Created Day
        self.page.get_by_role("heading", name="Order Created Day").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is not/are not").click()
        self.page.get_by_role("button", name="Select options...").first.click()
        self.page.get_by_role("option", name="Friday").click()
        self.page.get_by_role("option", name="Saturday").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Order Created Time
        self.page.get_by_role("heading", name="Order Created Time").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is greater or equal to").click()
        self.page.get_by_role("textbox", name="Value").nth(5).fill("10:20:00")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        ##################### Cart #####################
        self.page.get_by_role("heading", name="Cart").click()

        # Cart Items Count
        self.page.get_by_role("heading", name="Cart Items Count").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is greater or equal to").click()
        self.page.get_by_role("spinbutton").first.fill("2")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Cart Value
        self.page.get_by_role("heading", name="Cart Value").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is greater or equal to").click()
        self.page.get_by_role("spinbutton").nth(1).fill("20")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        ##################### Order #####################
        self.page.get_by_role("heading", name="Order").click()

        # Customer Locale
        self.page.get_by_role("heading", name="Customer Locale").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="starts with").click()
        self.page.get_by_role("button", name="Select an option").first.click()
        self.page.get_by_role("option", name="Bangla").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Financial Status
        self.page.get_by_role("heading", name="Financial Status").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is", exact=True).click()
        self.page.get_by_role("button", name="Select Value").click()
        self.page.get_by_role("option", name="Financial Status (Paid)").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Order Fulfillment Status
        self.page.get_by_role("heading", name="Order Fulfillment Status").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is", exact=True).click()
        self.page.get_by_role("button", name="Select Value").click()
        self.page.get_by_role("option", name="Fulfillment Status (fulfilled)").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Order Value
        self.page.get_by_role("heading", name="Order Value").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is greater or equal to").click()
        self.page.get_by_role("spinbutton").nth(2).fill("20")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Payment Method
        self.page.get_by_role("heading", name="Payment Method").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is/are").click()
        self.page.get_by_role("button", name="Selected Options").first.click()
        self.page.get_by_text("Cash on Delivery (COD)").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Shipping Country
        self.page.get_by_role("heading", name="Shipping Country").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is/are").click()
        self.page.get_by_role("button", name="Select options...").nth(1).click()
        self.page.get_by_text("Bangladesh").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Shipping Method
        self.page.get_by_role("heading", name="Shipping Method").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is/are").click()
        self.page.get_by_role("button", name="Selected Options").nth(1).click()
        self.page.get_by_text("Standard").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Currency
        self.page.get_by_role("heading", name="Currency").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is", exact=True).click()
        self.page.get_by_role("button", name="Select an option").nth(1).click()
        self.page.get_by_text("SGD").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Order Contains
        self.page.get_by_role("heading", name="Order Contains").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is/are").click()
        self.page.get_by_role("button", name="Selected Options").nth(2).click()
        self.page.get_by_text("Cappuccino").click()

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Tag Added On Customer
        self.page.get_by_role("heading", name="Tag Added On Customer").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is/are").click()
        self.page.get_by_role("textbox", name="Value").nth(6).fill("test_customer")

        self.page.locator("//div[2]/div/div[2]/div/div[2]/div[1]").click()

        # Tag Added On Order
        self.page.get_by_role("heading", name="Tag Added On Order").click()
        self.page.get_by_role("button", name="Select Item").click()
        self.page.get_by_role("option", name="is/are").click()
        self.page.get_by_role("textbox", name="Value").nth(7).fill("test_order")

        ##################### Condition end #####################
        self.page.get_by_role("button", name="Save Condition").click()

        ##################### Action start #####################
        self.page.get_by_text("Then", exact=True).click()

        ##################### General #####################
        self.page.get_by_test_id("rf__node-button").get_by_text("Action").click()
        self.page.get_by_role("heading", name="General").click()
        self.page.get_by_role("heading", name="delay representation").click()
        self.page.get_by_placeholder("Enter value (e.g. 4)").fill("1")
        self.page.get_by_role("button", name="Save Action").click()

        ##################### whatsapp #####################
        self.page.get_by_text("Delay", exact=True).click()
        self.page.get_by_test_id("rf__node-button").get_by_text("Action").click()
        self.page.get_by_role("heading", name="whatsapp").click()
        self.page.get_by_role("heading", name="Send Whatsapp Template").click()
        self.page.get_by_role("button", name="Select Whatsapp Channel").click()
        self.page.get_by_role("option", name="MyAlice (Dubai)").click()
        self.page.get_by_role("button", name="Select whatsapp template").click()
        self.page.get_by_role("option", name="test_101").click()
        self.page.get_by_role("button", name="Save Action").click()

        ##################### ecommerce #####################
        self.page.get_by_text("WhatsApp Template", exact=True).click()
        self.page.get_by_test_id("rf__node-button").get_by_text("Action").click()
        self.page.get_by_role("heading", name="ecommerce").click()
        self.page.get_by_role("heading", name="Add Tags on Customer").click()
        self.page.get_by_text("Add Variable").click()
        self.page.get_by_role("heading", name="order").click()
        self.page.get_by_text("{{checkout id}}").click()
        self.page.get_by_text("Add Variable").click()
        self.page.get_by_role("heading", name="contact").click()
        self.page.get_by_text("{{customer first name}}").click()
        self.page.get_by_role("button", name="Save Action").click()

        ##################### Action end #####################

        self.page.locator("//div/div/div/div/div[1]/div[2]/div/div/button").click()
        self.page.get_by_text("Save Automation").click()
        self.page.wait_for_timeout(3000)

    def add_delay_action(self):
        self.page.locator("//div[5]/div/div[1]/div[2]").click()
        self.page.get_by_text("Then", exact=True).click()
        self.page.get_by_test_id("rf__node-button").get_by_text("Action").click()
        self.page.get_by_role("heading", name="General").click()
        self.page.get_by_role("heading", name="delay representation").click()
        self.page.get_by_placeholder("Enter value (e.g. 4)").fill("5")
        self.page.get_by_role("button", name="Save Action").click()

    def edit_workflow_name(self, workflow_name_latest):
        self.page.locator("//main/div/div/div/div/div[1]/div[1]/button[2]").click()
        self.page.locator('input[name="form-title"]').fill(workflow_name_latest)
        self.page.get_by_text("Update Automation").click()
