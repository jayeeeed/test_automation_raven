import allure
import pytest
from pytest_bdd import given, when, then, scenario, parsers
from tests.base_test import login, dummy_obj
from pages.dashboard.create_agent_page import CreateAgentPage


# @pytest.mark.skip(reason="Skipping this test for now")
@allure.feature("Agent")
@allure.description("Create and connect agent to a channel")
@allure.severity(allure.severity_level.CRITICAL)
@scenario("../../features/agent.feature", "Create and connect agent to a channel")
def test_create_agent():
    pass


@given("I am logged in to the application")
@allure.step("Log in to the application")
def user_is_logged_in(page):
    # login(page)
    dummy_obj(page)


@when(parsers.parse("I create an custom agent {name} with description {description}"))
@allure.step("Create an custom agent {name} with description {description}")
def create_agent1(page, name, description):
    create_agent_page = CreateAgentPage(page)
    create_agent_page.create_agent(name, description)
    create_agent_page.ticket_tool()
    create_agent_page.agent_test()


@when(parsers.parse("I should able to connect to a channel"))
@allure.step("Connect to a channel")
def connect_channel(page):
    create_agent_page = CreateAgentPage(page)
    create_agent_page.deploy_agent()
