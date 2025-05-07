import allure
import pytest
from tests.base_test import login
from pages.inbox.chatbox_page import ChatboxPage


@pytest.mark.skip(reason="Skipping this test for now")
@allure.feature("Chatbox Functionality")
@allure.story("User sends message via chatbox")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://your_project_tracking_url", name="Project Tracking Link")
@allure.description(
    "This test verifies that the user can send a message via the chatbox after logging in."
)
def test_chatbox(browser_context):
    page = browser_context

    with allure.step("Log in to the application"):
        login(page)

    with allure.step("Load configuration and navigate to chatbox"):
        chatbox_page = ChatboxPage(page)
        chatbox_page.goto_chatbox()

    with allure.step("Apply filters"):
        # chatbox_page.apply_filters()
        chatbox_page.save_view()
        # chatbox_page.select_view()
        # chatbox_page.delete_view()

    with allure.step("Automation starts here..."):
        chatbox_page.text_send("Automation Starts here...")

    with allure.step("Send attachments and verify delivery"):
        chatbox_page.upload_image("e2e/data/images/2mb.jpg", "e2e/data/images/6mb.jpg")
        chatbox_page.upload_video("e2e/data/videos/2mb.mp4", "e2e/data/videos/8mb.mp4")
        chatbox_page.upload_audio("e2e/data/audios/1mb.mp3")
        chatbox_page.upload_document("e2e/data/documents/1mb.pdf")

    with allure.step("Send recording and verify delivery"):
        chatbox_page.upload_recording("e2e/data/audios/1mb.mp3")

    with allure.step("Add product to cart"):
        chatbox_page.add_to_cart()
        chatbox_page.order_form()
        chatbox_page.place_order()
        chatbox_page.order_confirmation()

    with allure.step("Send saved reply"):
        chatbox_page.send_saved_reply()

    with allure.step("Send note"):
        chatbox_page.send_note()

    with allure.step("Assign ticket"):
        chatbox_page.assign_ticket()
        chatbox_page.delete_view()

    with allure.step("Top bar functionalities"):
        chatbox_page.copy_link()
        chatbox_page.change_priority()
        chatbox_page.add_tag()

    with allure.step("Left bar functionalities"):
        chatbox_page.search_ticket()
        chatbox_page.bulk_assign()
        chatbox_page.compose_wa()
        chatbox_page.sort_tickets()
        chatbox_page.pin_ticket()
        chatbox_page.edit_attribute()
        chatbox_page.reopen_ticket()

    with allure.step("Automation ends here..."):
        chatbox_page.text_send("Automation ends here...")

    allure.attach(
        page.screenshot(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
