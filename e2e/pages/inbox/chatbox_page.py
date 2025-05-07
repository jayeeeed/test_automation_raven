import re
from playwright.sync_api import Page, expect
from utils.config_loader import load_config


class ChatboxPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_chatbox(self):
        config = load_config()
        base_url = config["base_url"]

        self.page.locator("//button[3]").click()
        self.page.wait_for_url(f"{base_url}/projects/**/inbox")

        self.page.wait_for_timeout(5000)
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        self.page.wait_for_timeout(1000)

    def text_send(self, message: str):
        self.page.locator("[id='reply-input']").fill(message)
        self.page.get_by_role("button", name="Send").click()

    def text_confirm(self, message: str):
        sent_msg = self.page.locator("[data-testid='text-message-block']").first
        expect(sent_msg).to_have_text(message)

    def upload_file(self, file_type: str, file_paths: list):
        self.page.locator("[data-for='attachment']").click()
        self.page.get_by_role("button", name=f"{file_type}", exact=True).click()

        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Upload").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_paths)

        self.page.get_by_role("button", name="Send 1 file").click()
        self.page.locator("[class='uppy-Dashboard-innerWrap']").wait_for(state="hidden")

    def upload_image(self, *image_paths: str):
        self.upload_file("Image", list(image_paths))

    def upload_video(self, *video_paths: str):
        self.upload_file("Video", list(video_paths))

    def upload_audio(self, *audio_paths: str):
        self.upload_file("Audio", list(audio_paths))

    def upload_document(self, *document_paths: str):
        self.upload_file("Document", list(document_paths))

    def upload_recording(self, *recording_paths: str):
        self.page.locator("[data-for='audio']").click()

        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Upload Audio").click()
        file_chooser = fc_info.value
        file_chooser.set_files(recording_paths)

        self.page.get_by_role("button", name="Send 1 file").click()
        self.page.locator("[class='uppy-Dashboard-innerWrap']").wait_for(state="hidden")

    def add_to_cart(self):
        self.page.locator("[data-for='ecommerce']").click()
        self.page.locator("[id='7395914449082_0']").check()
        self.page.get_by_role("button", name="Add to cart (1)").click()
        self.page.get_by_placeholder("Select Variation").click()
        self.page.locator("//span[contains(text(), 'Default Title')]").click()
        self.page.get_by_role("button", name="Checkout").click()

    def order_form(self):
        self.page.locator('input[name="billing_address"]').check()
        self.page.get_by_placeholder("ex: John").first.fill("Jayed")
        self.page.get_by_placeholder("ex: John").nth(1).fill("Bin Jahangir")
        self.page.get_by_placeholder("ex: johndoe@email.com").fill("jayed@myalice.ai")
        self.page.get_by_placeholder("Phone number with country code").fill(
            "+8801756260844"
        )
        self.page.locator('input[name="address_one"]').fill("Dhaka")
        self.page.locator('input[name="address_two"]').fill("123/dhaka")
        self.page.locator('input[name="city"]').fill("Dhaka")
        self.page.locator('input[name="state"]').fill("Dhaka")
        self.page.locator('input[name="postcode"]').fill("1206")
        self.page.get_by_text("Saudi Arabia - Rial").click()
        self.page.get_by_text("Bangladesh - Taka").click()
        # self.page.get_by_role("checkbox", name="Same as shipping information").click()
        self.page.get_by_text("Next").click()

    def place_order(self):
        self.page.get_by_text("Select Delivery Method").click()
        self.page.get_by_text("Free shipping").click()
        self.page.get_by_text("Select Discount Type").click()
        self.page.get_by_text("PERCENTAGE").click()
        self.page.locator("//div[3]/div[2]/input").fill("20")
        self.page.get_by_placeholder("Reason for discount").fill("DISCOUNT20")
        self.page.locator("span.ease-in-out").click()
        self.page.get_by_text("Next").click()

    def order_confirmation(self):
        self.page.locator("svg.text-opacity-70").click()
        self.page.locator("//p[contains(text(), 'Paid Order')]").click()
        self.page.get_by_text("completed Order", exact=True).click()
        self.page.get_by_text("Send Checkout Link").click()

    def verify_order_link(self, link: str):
        sent_msg = self.page.locator("[data-testid='text-message-block']").first
        pattern = re.compile(f".*{re.escape(link)}.*")
        expect(sent_msg).to_have_text(pattern)

    def send_saved_reply(self):
        self.page.locator("[data-for='savedReply']").click()
        self.page.locator("//div[3]/div/div/div/div[2]/div/div[1]/p").click()
        self.page.get_by_role("button", name="Send").click()

    def send_note(self):
        self.page.locator("//span[contains(text(), 'Note')]").click()
        self.page.locator("[id='reply-input']").fill("Save note success")
        self.page.locator("//div[3]/div[2]/div/div[2]/div/button").click()
        self.page.locator("//span[contains(text(), 'Chat')]").click()

    def set_filters(self):
        self.page.get_by_text("Filter", exact=True).click()

        self.page.get_by_role("textbox", name="Select Channels").click()
        self.page.get_by_text("Automation Page").first.click()
        self.page.get_by_role("button", name="Select").click()

        self.page.get_by_role("textbox", name="Select Agents").click()
        self.page.get_by_test_id("leftbar-id").get_by_text("Jayed Bin Jahangir").click()
        self.page.get_by_role("button", name="Select").click()

        self.page.get_by_role("textbox", name="Select Groups").click()
        self.page.get_by_test_id("leftbar-id").get_by_text(
            "Test Automation", exact=True
        ).click()
        self.page.get_by_role("button", name="Cancel").click()

        self.page.get_by_role("textbox", name="Select Tags").click()
        self.page.get_by_test_id("leftbar-id").get_by_text(
            "test123", exact=True
        ).click()
        self.page.get_by_role("button", name="Select").click()

        self.page.get_by_role("textbox", name="Select Priorities").click()
        self.page.locator("//div/div[2]/span[2][contains(text(), 'Urgent')]").click()
        self.page.get_by_role("button", name="Select").click()

        self.page.get_by_role("textbox", name="From").fill("January 1, 2025 12:00 AM")
        self.page.get_by_role("textbox", name="To").fill("December 31, 2025 11:50 PM")

    def apply_filters(self):
        self.set_filters()
        self.page.get_by_role("button", name="Apply Filters").click()

    def save_view(self):
        self.set_filters()
        self.page.get_by_role("button", name="Save as View").click()
        self.page.locator("[id='alice-textFiled']").fill("automation")
        self.page.get_by_role("button", name="Save for yourself").click()

    def delete_view(self):
        self.page.wait_for_load_state("networkidle")
        self.page.reload(wait_until="networkidle")
        self.page.locator("//span[contains(text(), 'All Assigned')]").click()
        self.page.get_by_test_id("leftbar-id").get_by_text(
            "automation", exact=True
        ).click()
        self.page.get_by_text("Filter Applied").click()
        self.page.get_by_text("Delete").click()
        self.page.get_by_label("Delete Saved View?").get_by_role(
            "button", name="Delete"
        ).click()
        self.page.wait_for_load_state("networkidle")

    def select_view(self):
        self.page.locator("//span[contains(text(), 'All Assigned')]").click()
        self.page.locator("//span[contains(text(), 'jayed')]").click()

    def assign_ticket(self):
        self.page.get_by_role("button", name="icon_box You").click()
        self.page.get_by_role("checkbox", name="icon_box You").click()
        self.page.locator("//p[contains(text(), 'imu 15 stage')]").click()
        self.page.get_by_role("textbox", name="Add a note for your teammates").fill(
            "test comment"
        )
        self.page.get_by_test_id("middle-top-bar").locator("button").filter(
            has_text="Assign"
        ).click()
        self.page.wait_for_timeout(2000)
        self.page.reload(wait_until="domcontentloaded")
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("button", name="Assign to me").click()

    def copy_link(self):
        self.page.locator("[data-for='copy-link']").click()
        self.page.locator("[id='reply-input']").click()
        self.page.keyboard.press("ControlOrMeta+KeyV")
        self.page.get_by_role("button", name="Send").click()

    def change_priority(self):
        self.page.get_by_role("button", name="Urgent").click()
        self.page.get_by_role("menuitem", name="Low").click()
        self.page.get_by_role("button", name="Low").click()
        self.page.get_by_role("menuitem", name="Urgent").click()

    def add_tag(self):
        self.page.locator("//*[@id='leftmost-elements']/div[1]/button").click()
        self.page.get_by_role("textbox", name="Search or add new tags").fill("test123")
        self.page.get_by_text("as a new tag.").click()

    def search_ticket(self):
        self.page.locator("//div[2]/button[3]").click()
        self.page.get_by_role(
            "combobox", name="Search by name, email or phone number"
        ).fill("automation test")
        self.page.locator("//div[1]/span[contains(text(), 'automation test')]").click()
        self.page.locator("[id='reply-input']").fill("search success")
        self.page.get_by_role("button", name="Send").click()
        self.page.reload(wait_until="domcontentloaded")
        self.page.wait_for_timeout(2000)

    def bulk_assign(self):
        self.page.locator("//div[2]/button[2]").click()
        self.page.get_by_role("button", name="Select All").click()
        # self.page.get_by_role("button", name="Unselect All").click()
        # self.page.get_by_role("button", name="Close Chat").click()
        # self.page.get_by_role("button", name="Assign").click()
        self.page.get_by_role("button", name="Exit Select Mode").click()

    def compose_wa(self):
        # self.page.locator("//div[2]/button[1]").click()
        self.page.locator("//div[1]/div[1]/div[1]/div[2]/button[1]").click()
        self.page.get_by_role("combobox", name="Enter WhatsApp number").fill(
            "01756260844"
        )
        self.page.get_by_role("option", name="MyAlice (Dubai)").click()
        self.page.get_by_role("combobox", name="WhatsApp Channel*").click()
        self.page.get_by_role("option", name="MyAlice (Dubai)").click()
        self.page.get_by_role("button", name="Create").click()
        self.page.get_by_role("button", name="Send a message template").click()
        self.page.locator("//p[contains(text(), 'test_101')]").click()
        self.page.get_by_role("button", name="Send Message").click()

    def sort_tickets(self):
        self.page.get_by_text("Newest", exact=True).click()
        self.page.get_by_role("button", name="Showing oldest tickets first").click()
        self.page.get_by_text("Oldest", exact=True).click()
        self.page.get_by_role("button", name="Showing newest tickets first").click()

    def pin_ticket(self):
        self.page.locator("//*[@id='ticket-list-bar']/div[4]/div/span").click()
        self.page.wait_for_timeout(500)
        self.page.locator("//*[@id='ticket-list-bar']/div[1]/div/span").click()

    def edit_attribute(self):
        self.page.get_by_role("img", name="left-collapse").click()
        self.page.get_by_role("textbox", name="Add full name").fill("automation test")
        self.page.keyboard.press("Enter")
        self.page.get_by_role("textbox", name="Add email").fill("jayed@myalice.ai")
        self.page.keyboard.press("Enter")
        self.page.get_by_placeholder("Add phone").fill("01756260844")
        self.page.keyboard.press("Enter")
        self.page.get_by_role("textbox", name="Add new attribute").fill("automation")
        self.page.get_by_text("as a new attribute.").click()
        self.page.locator(
            "//div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[2]/input"
        ).fill("success")
        self.page.keyboard.press("Enter")

    def reopen_ticket(self):
        self.page.locator("//span[contains(text(), 'All Assigned')]").click()
        self.page.locator("//span[contains(text(), 'All Closed')]").click()
        self.page.get_by_role("button", name="Open Chat").click()
        self.page.get_by_role("checkbox", name="icon_box You").click()
        self.page.get_by_role("textbox", name="Add a note for your teammate...").fill(
            "reopen comment"
        )
        self.page.get_by_test_id("middle-top-bar").locator("button").filter(
            has_text="Reopen"
        ).click()
        self.page.wait_for_timeout(2000)
        self.page.reload(wait_until="domcontentloaded")
        self.page.wait_for_timeout(2000)
        self.page.locator("//*[@id='ticket-list-bar']/div[3]").click()
        self.page.get_by_role("button", name="Send a message template").click()
        self.page.locator("//p[contains(text(), 'test_101')]").click()
        self.page.get_by_role("button", name="Send Message").click()
        self.page.locator("//*[@id='ticket-list-bar']/div[1]").click()
