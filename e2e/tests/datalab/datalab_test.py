import allure
import pytest
from pages.datalab.datalab_page import DatalabPage
from tests.base_test import login
from utils.config_loader import load_config


@pytest.mark.skip(reason="Skip this test for now!")
@allure.feature("Datalab Functionality")
@allure.story("User creates,updates and deletes datalab")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://your_project_tracking_url", name="Project Tracking Link")
@allure.description(
    "This test verifies that user can create, update and delete datalab."
)
def test_datalab(browser_context):
    page = browser_context

    with allure.step("Log in to the application"):
        login(page)

    with allure.step("Load configuration and navigate to datalab"):
        datalab_page = DatalabPage(page)
        config = load_config()
        base_url = config["base_url"]
        datalab_page.goto_datalab()
        page.wait_for_url(f"{base_url}/projects/1982/data-lab")
        page.wait_for_timeout(4000)

    with allure.step("Create datalab"):
        datalab_page.create_datalab(
            "Test Datalab", "This is a test datalab", "e2e/data/images/2mb.jpg", "Save"
        )
        page.wait_for_timeout(4000)

    with allure.step("Enter Text Inputs"):
        datalab_page.insert_text_inputs(
            "Text", "First Name", "Name", "Enter your first name", "customer first name"
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_text_inputs(
            "Paragraph",
            "Description",
            "Description",
            "Enter your details",
            "customer details",
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_text_inputs(
            "Number", "Age", "Age", "Enter your age", "customer age"
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_text_inputs(
            "Phone", "Mobile", "Mobile", "Enter your mobile no.", "customer mobile no."
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_text_inputs(
            "Email", "Email", "Email", "Enter your email", "customer email"
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_text_inputs(
            "URL",
            "Linkedin",
            "Linkedin",
            "Enter your linkedin url",
            "customer linkedin url",
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_text_inputs(
            "Date/Time", "Purchase Date", "Purchase Date", None, "purchase date"
        )
        page.wait_for_timeout(2000)

    with allure.step("Enter Media Inputs"):
        datalab_page.insert_media_inputs(
            "Image",
            "Profile",
            "Profile",
            "Upload or drag & drop your image here",
            "Upload your profile picture",
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_media_inputs(
            "Video",
            "Demo Video",
            "Demo Video",
            "Upload or drag & drop your video here",
            "Upload your video",
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_media_inputs(
            "File",
            "Attachment",
            "Attachment",
            "Upload or drag & drop your file here",
            "Upload your file",
        )
        page.wait_for_timeout(2000)

    with allure.step("Enter Multiple Choice Inputs"):
        datalab_page.insert_multiple_choice_inputs(
            "Multi-Select",
            "Favourite Color",
            "Favourite Color",
            "Select your favourite colors",
            "customer favourite colors",
        )
        page.wait_for_timeout(2000)

        datalab_page.insert_multiple_choice_inputs(
            "Single Select", "Gender", "Gender", "Select your gender", "customer gender"
        )
        page.wait_for_timeout(2000)

    with allure.step("Enter Group Inputs"):
        datalab_page.insert_group_inputs("Enter item name", "Enter item quantity")
        page.wait_for_timeout(4000)

    with allure.step("Edit datalab info"):
        page.goto(f"{base_url}/projects/1982/data-lab")
        datalab_page.edit_datalab_info()

    with allure.step("Enter into Datalab"):
        datalab_page.enter_datalab_section()

    with allure.step("Download Sample Data"):
        datalab_page.download_sample_data()

    with allure.step("Create Datalab Entry"):
        datalab_page.create_datalab_entry(
            "Jubair Ahmed Khan",
            "I am working at MyALice",
            "28",
            "+8801712345678",
            "6f6Zw@example.com",
            "https://www.linkedin.com/in",
        )

    with allure.step("Import data to datalab"):
        page.wait_for_timeout(4000)
        datalab_page.import_datalab_data("e2e/data/csv/test_data.csv")

    with allure.step("Delete single datalab entry"):
        page.wait_for_timeout(4000)
        datalab_page.delete_single_datalab_entry()

    with allure.step("Delete datalab"):
        page.goto(f"{base_url}/projects/1982/data-lab")
        datalab_page.delete_datalab()

    page.wait_for_timeout(5000)

    allure.attach(
        page.screenshot(),
        name="Facebook Feed Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
