import allure
import pytest
from pytest_bdd import given, when, then, scenario, parsers
from tests.base_test import login
from pages.dashboard.create_agent_page import CreateAgentPage


# @pytest.mark.skip(reason="Skipping this test for now")
@allure.feature("Agent")
@allure.description("Create Agent")
@allure.severity(allure.severity_level.CRITICAL)
@scenario("../../features/agent.feature", "Create Agent")
def test_create_agent():
    pass


@given("I am logged in to the application")
@allure.step("Log in to the application")
def user_is_logged_in(page):
    login(page)


@when(parsers.parse("I create a custom agent {name} with description {description}"))
@allure.step("Create a custom agent {name} with description {description}")
def create_agent1(page, name, description, tool_info):
    create_agent_page = CreateAgentPage(page)
    create_agent_page.create_agent(name, description)
    create_agent_page.ticket_tool(tool_info)
    create_agent_page.agent_test()


@then(parsers.parse("I should able to connect to {channel}"))
@allure.step("Connect to {channel}")
def connect_channel(page):
    create_agent_page = CreateAgentPage(page)
    create_agent_page.deploy_agent()
