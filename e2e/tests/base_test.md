# Base Test

This file, `base_test.py`, contains the base functionality for logging into the application. It is used as a helper function in other test files to perform the login operation before executing specific tests.

## Functions

### `login(browser_context)`

This function logs into the application using the provided browser context. It performs the following steps:

1. Loads the configuration and login data from the respective JSON files.
2. Extracts the base URL, email, and password from the loaded data.
3. Initializes the `LoginPage` object with the browser context.
4. Navigates to the base URL.
5. Performs the login operation using the provided email and password.
6. Waits for the URL to change to the dashboard page after a successful login.

## Usage

The `login` function is used in other test files to ensure that the user is logged into the application before performing any specific test actions. Here is an example of how it is used in a test file:

```python
from tests.base_test import login

def test_example(browser_context):
    page = browser_context

    # Log in to the application
    login(page)

    # Perform specific test actions
    # ...