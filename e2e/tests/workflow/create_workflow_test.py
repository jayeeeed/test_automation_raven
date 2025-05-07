import allure
import pytest
from pytest_bdd import given, when, then, scenario, parsers
from tests.base_test import login
from pages.workflow.workflow_dashboard_page import WorkflowDashboardPage
from pages.workflow.workflow_create_page import WorkflowCreatePage


@pytest.mark.skip(reason="Skipping this test for now")
@allure.feature("Workflow")
@allure.description("User creates a workflow")
@allure.severity(allure.severity_level.CRITICAL)
@scenario("../../features/workflow.feature", "Create workflow")
def test_create_workflow():
    pass


@given("I am logged in to the application")
@allure.step("Log in to the application")
def user_is_logged_in(page):
    login(page)


@when("I navigate to the workflow")
@allure.step("Navigate to workflow")
def navigate_to_workflow_dashboard(page):
    workflow_dashboard_page = WorkflowDashboardPage(page)
    workflow_dashboard_page.goto_workflow()


@when(parsers.parse('I create a new workflow "{workflow_name}"'))
@allure.step("Create a new workflow {workflow_name}")
def create_workflow(page, workflow_name):
    workflow_create_page = WorkflowCreatePage(page)
    workflow_create_page.create_workflow(workflow_name)


@then(parsers.parse('I should see the "{workflow_name}" in the dashboard'))
@allure.step("Verify {workflow_name} in dashboard")
def verify_workflow_in_dashboard(page, workflow_name):
    workflow_dashboard_page = WorkflowDashboardPage(page)
    workflow_dashboard_page.verify_workflow(workflow_name)


@then(parsers.parse('I add a delay action to the "{workflow_name}"'))
@allure.step("Add a delay action to the {workflow_name}")
def edit_workflow(page, workflow_name):
    workflow_create_page = WorkflowCreatePage(page)
    workflow_dashboard_page = WorkflowDashboardPage(page)

    workflow_dashboard_page.edit_workflow(workflow_name)
    workflow_create_page.add_delay_action()


@then(parsers.parse('I save the workflow as "{workflow_name_latest}"'))
@allure.step("Save the workflow as {workflow_name_latest}")
def edit_workflow_name(page, workflow_name_latest):
    workflow_create_page = WorkflowCreatePage(page)
    workflow_create_page.edit_workflow_name(workflow_name_latest)


@then(
    parsers.parse('I should see the updated "{workflow_name_latest}" in the dashboard')
)
@allure.step("Verify updated {workflow_name_latest} in dashboard")
def verify_updated_workflow_in_dashboard(page, workflow_name_latest):
    workflow_dashboard_page = WorkflowDashboardPage(page)
    workflow_dashboard_page.verify_workflow(workflow_name_latest)
