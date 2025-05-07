import allure
import pytest
from pytest_bdd import given, when, then, scenario, parsers
from tests.base_test import login
from pages.inbox.chatbox_page import ChatboxPage


# @pytest.mark.skip(reason="Skipping this test for now")
@allure.feature("Inbox")
@allure.description("User send message")
@allure.severity(allure.severity_level.CRITICAL)
@scenario("../../features/inbox.feature", "Send message")
def test_send_message():
    pass


@given("I am logged in to the application")
@allure.step("Log in to the application")
def user_is_logged_in(page):
    login(page)


@when("I navigate to the inbox")
@allure.step("Navigate to inbox")
def navigate_to_chatbox(page):
    chatbox_page = ChatboxPage(page)
    chatbox_page.goto_chatbox()


@when(parsers.parse("I send a message {message}"))
@allure.step("Send message {message}")
def send_message(page, message):
    chatbox_page = ChatboxPage(page)
    chatbox_page.text_send(message)


@then(parsers.parse("I should see the {message} in the inbox"))
@allure.step("Verify {message} in the inbox")
def verify_delivery(page, message):
    chatbox_page = ChatboxPage(page)
    chatbox_page.text_confirm(message)
