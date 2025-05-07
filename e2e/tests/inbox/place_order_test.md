# Inbox Order Placement Test

This test file, `test_place_order.py`, is designed to verify the functionality of placing an order and sending the order link via the inbox feature of the application. The test is implemented using the `pytest` and `pytest-bdd` frameworks, with steps structured to simulate the order placement process and validate the order link delivery.

## Test Scenarios

The test covers the following scenario:

* Place an order and send the order placement link to the customer.

## Test Steps

The test performs the following steps:

1. Logs in to the application.
2. Navigates to the inbox page.
3. Completes the order placement process.
4. Sends the order placement link to the customer.
5. Verifies that the order link is visible in the inbox.

## Requirements

* The test requires valid login credentials to access the application.
* The order placement functionality must be available and accessible.
* The inbox must support sending and displaying order links.
* All necessary dependencies for `pytest`, `pytest-bdd`, and `allure` must be installed.

## Running the Test

To run the test, use the following command:

```bash
pytest path/to/test_place_order.py
```

To generate and view the Allure report:

```bash
allure serve results
```