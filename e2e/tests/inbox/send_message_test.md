# Inbox Message Test

This test file, `test_send_message.py`, is designed to verify the functionality of sending a message in the inbox feature of the application. The test is implemented using the `pytest` and `pytest-bdd` frameworks, with steps organized to simulate and validate message sending.

## Test Scenarios

The test covers the following scenario:

* Send a message and verify that it appears in the inbox.

## Test Steps

The test performs the following steps:

1. Logs in to the application.
2. Navigates to the inbox page.
3. Sends a message.
4. Verifies that the sent message appears in the inbox.

## Requirements

* The test requires valid login credentials to access the application.
* The inbox feature must be available and accessible.
* All necessary dependencies for `pytest`, `pytest-bdd`, and `allure` must be installed.

## Running the Test

To run the test, use the following command:

```bash
pytest path/to/test_send_message.py
```

To generate and view the Allure report:

```bash
allure serve results
```