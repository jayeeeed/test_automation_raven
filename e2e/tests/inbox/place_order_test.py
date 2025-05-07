import allure
import pytest
from pytest_bdd import given, when, then, scenario, parsers
from tests.base_test import login
from pages.inbox.chatbox_page import ChatboxPage


@pytest.mark.skip(reason="Skipping this test for now")
@allure.feature("Inbox")
@allure.description("User place order")
@allure.severity(allure.severity_level.CRITICAL)
@scenario("../../features/inbox.feature", "Place order")
def test_place_order():
    pass


@given("I am logged in to the application")
@allure.step("Log in to the application")
def user_is_logged_in(page):
    login(page)


@when("I navigate to the inbox")
@allure.step("Navigate to chatbox")
def navigate_to_chatbox(page):
    chatbox_page = ChatboxPage(page)
    chatbox_page.goto_chatbox()


@when("I complete the order placement")
@allure.step("Complete order placement")
def place_order(page):
    chatbox_page = ChatboxPage(page)
    chatbox_page.add_to_cart()
    chatbox_page.order_form()
    chatbox_page.place_order()


@then("I send the order placement link to customer")
@allure.step("Send order placement link to customer")
def send_order_placement_link(page):
    chatbox_page = ChatboxPage(page)
    chatbox_page.order_confirmation()


@then(parsers.re(r"I should see the order link in the inbox '(?P<link_partial>.+)'"))
@allure.step("Verify order link in inbox")
def verify_order_link_in_inbox(page, link_partial):
    chatbox_page = ChatboxPage(page)
    chatbox_page.verify_order_link(link_partial)
