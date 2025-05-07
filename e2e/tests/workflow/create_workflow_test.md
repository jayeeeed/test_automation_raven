# Create Workflow Test

This test file, `create_workflow_test.py`, is designed to verify the functionality of creating a workflow in the application. The test is implemented using the Pytest and Pytest-BDD frameworks.

## Test Scenarios

The test covers the following scenario:

* Create a new workflow

## Test Steps

The test performs the following steps:

1. Logs in to the application
2. Navigates to the workflow dashboard page
3. Creates a new workflow

## Requirements

* The test requires a valid login credentials to access the application
* The test requires the workflow feature to be enabled in the application

## Running the Test

To run the test, use the following command:

```bash
pytest e2e/tests/workflow/create_workflow_test.py