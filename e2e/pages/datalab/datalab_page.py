from playwright.sync_api import Page


class DatalabPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_datalab(self):
        self.page.wait_for_timeout(2000)
        self.page.locator("#teamImage").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_text("Jubair Ahmed Khan's Team").click()
        self.page.wait_for_timeout(3000)
        self.page.click("//button[9]")

    def create_datalab(
        self, title: str, description: str, image: str, button_text: str
    ):
        self.page.get_by_text("Create Datalab").click()
        self.page.get_by_placeholder("Lab Title").fill(title)
        self.page.get_by_placeholder("Provide A valid Description").fill(description)
        self.page.set_input_files("//section/div/input", files=[image])
        self.page.get_by_placeholder("Button Text").fill(button_text)
        self.page.get_by_text("Create Data Lab").click()

    def insert_text_inputs(
        self,
        input_type: str,
        customer_label: str,
        agent_label: str | None = None,
        placeholder: str | None = None,
        help_text: str | None = None,
    ):
        self.page.locator(f"//span[text()='{input_type}']").click()

        self.page.locator("#name").fill(customer_label)

        if agent_label:
            self.page.locator("#label_agent").fill(agent_label)
        if input_type != "Date/Time":
            if placeholder:
                self.page.get_by_placeholder("Enter placeholder").fill(placeholder)
        if help_text:
            self.page.get_by_placeholder("Enter help text").fill(help_text)

        self.page.get_by_label("Set as required").click()
        self.page.locator('button:has-text("Save Changes")').click()

    def insert_media_inputs(
        self,
        input_type: str,
        customer_label: str,
        agent_label: str | None = None,
        placeholder_text: str | None = None,
        placeholder: str | None = None,
    ):
        self.page.locator(f"//span[text()='{input_type}']").click()

        self.page.locator("#name").fill(customer_label)

        if agent_label:
            self.page.locator("#label_agent").fill(agent_label)
        if input_type != "Date/Time":
            if placeholder:
                self.page.get_by_placeholder(placeholder_text).fill(placeholder)

        self.page.get_by_label("Set as required").click()
        self.page.locator('button:has-text("Save Changes")').click()

    def insert_multiple_choice_inputs(
        self,
        input_type: str,
        customer_label: str,
        agent_label: str | None = None,
        placeholder: str | None = None,
        help_text: str | None = None,
    ):
        self.page.locator(f"//span[text()='{input_type}']").click()

        self.page.locator("#name").fill(customer_label)

        if agent_label:
            self.page.locator("#label_agent").fill(agent_label)
        if placeholder:
            self.page.get_by_placeholder("Enter placeholder").fill(placeholder)
        if help_text:
            self.page.get_by_placeholder("Enter help text").fill(help_text)

        if input_type == "Multi-Select":
            self.page.get_by_placeholder("Add options").fill("Red")
            self.page.locator("//div[3]/button").click()

            self.page.get_by_placeholder("Add options").fill("Green")
            self.page.locator("//div[5]/button").click()

            self.page.get_by_placeholder("Add options").fill("Blue")
            self.page.locator("//div[7]/button").click()
        else:
            self.page.get_by_placeholder("Add options").fill("Male")
            self.page.locator("//div[3]/button").click()

            self.page.get_by_placeholder("Add options").fill("Female")
            self.page.locator("//div[5]/button").click()

            self.page.get_by_placeholder("Add options").fill("Others")
            self.page.locator("//div[7]/button").click()

        self.page.get_by_label("Set as required").click()
        self.page.locator('button:has-text("Save Changes")').click()

    def insert_group_inputs(self, ph1: str, ph2: str):
        self.page.locator("//span[text()='Group']").click()

        self.page.wait_for_timeout(3000)
        self.page.locator("svg.lucide-grip-vertical").last.click()
        text_input = self.page.locator("//span[text()='Text']")
        group_input1 = self.page.locator(".dropZone").nth(-2)
        text_input.drag_to(group_input1, force=True)

        self.page.wait_for_timeout(3000)
        self.page.locator("svg.lucide-grip-vertical").last.click()
        self.page.locator("#name").fill("Item Name")
        self.page.get_by_placeholder("Enter placeholder").fill(ph1)
        self.page.get_by_label("Set as required").click()
        self.page.locator('button:has-text("Save Changes")').click()

        self.page.wait_for_timeout(3000)
        number_input = self.page.locator("//span[text()='Number']")
        group_input2 = self.page.locator(".dropZone").nth(-2)
        number_input.drag_to(group_input2, force=True)

        self.page.wait_for_timeout(3000)
        self.page.locator("svg.lucide-grip-vertical").last.click()
        self.page.locator("#name").fill("Quantity")
        self.page.get_by_placeholder("Enter placeholder").fill(ph2)
        self.page.get_by_label("Set as required").click()
        self.page.locator('button:has-text("Save Changes")').click()

    def edit_datalab_info(self):
        self.page.wait_for_timeout(3000)
        self.page.locator("span.sr-only").nth(1).click()
        self.page.locator('//span[text()="Edit Info"]').click()
        self.page.get_by_placeholder("Lab Title").fill("Testing Datalab")
        self.page.get_by_placeholder("Button Text").fill("Store")
        self.page.locator('//span[text()="Update"]').click()

    def enter_datalab_section(self):
        self.page.wait_for_timeout(5000)
        self.page.locator('//h3[text()="Testing Datalab"]').click()

    def download_sample_data(self):
        self.page.get_by_text("Download sample data").click()

    def create_datalab_entry(
        self,
        first_name: str,
        description: str,
        age: str,
        mobile: str,
        email: str,
        url: str,
    ):
        self.page.get_by_role("button", name="Create New Entry").click()

        self.page.get_by_placeholder("Enter your first name").fill(first_name)
        self.page.get_by_placeholder("Enter your details").fill(description)
        self.page.get_by_placeholder("Enter your age").fill(age)
        self.page.get_by_placeholder("Enter your mobile no.").fill(mobile)
        self.page.get_by_placeholder("Enter your email").fill(email)
        self.page.get_by_placeholder("Enter your linkedin url").fill(url)
        self.page.get_by_text("Pick a date & time").click()
        self.page.get_by_role("gridcell", name="1", exact=True).first.click()
        self.page.keyboard.press("Escape")

        self.upload_file("e2e/data/images/2mb.jpg", "svg.lucide-image")
        self.upload_file("e2e/data/videos/2mb.mp4", "svg.lucide-video")
        self.upload_file("e2e/data/documents/1mb.pdf", "svg.lucide-file-text")

        self.page.get_by_text("Select your favourite colors").click()
        self.page.get_by_role("option", name="Red").click()
        self.page.get_by_role("option", name="Green").click()
        self.page.get_by_role("option", name="Blue").click()
        self.page.keyboard.press("Escape")

        self.page.locator('span:has-text("Select your gender")').click()
        self.page.get_by_role("option", name="Male", exact=True).click()

        self.page.get_by_placeholder("Enter item name").fill("Mobile")
        self.page.get_by_placeholder("Enter item quantity").fill("5")

        self.page.wait_for_timeout(3000)
        self.page.locator("//button[contains(text(), 'Store')]").click()

    def upload_file(self, file_path: str, dropzone: str):
        with self.page.expect_file_chooser() as fc_info:
            self.page.locator(dropzone).click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def import_datalab_data(self, file_path: str):
        self.page.wait_for_timeout(3000)
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Import").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def delete_single_datalab_entry(self):
        self.page.locator("tr:nth-child(1) > td > .mr-2").click()
        self.page.get_by_text("Delete").click()
        self.page.get_by_label("Delete 1 Entries").get_by_role(
            "button", name="Yes! Delete"
        ).click()

    def delete_datalab(self):
        self.page.locator("span.sr-only").nth(1).click()
        self.page.locator('//span[text()="Delete"]').click()
        self.page.locator('//span[text()="Confirm"]').click()
