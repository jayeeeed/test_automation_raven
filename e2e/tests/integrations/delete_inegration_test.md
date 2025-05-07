# Delete Integration Test

This test file, `delete_inegration_test.py`, is designed to verify the functionality of deleting integrations in the application. The test is implemented using the Playwright and Pytest frameworks, and it includes steps to log in to the application, navigate to the integrations page, and delete specific integrations.

## Test Steps

1. **Log in to the application:**
   - The test starts by logging in to the application using the credentials provided in the configuration files.

2. **Load configuration and navigate to integrations:**
   - The test loads the configuration settings and navigates to the integrations page.

3. **Delete integrations:**
   - The test deletes specific integrations from the integrations page.

4. **Attach screenshot:**
   - A screenshot of the page is taken and attached to the test report for verification.

## File Structure

- `e2e/tests/integrations/delete_inegration_test.py`: The main test file containing the delete integration test.
- `e2e/pages/integrations/integrated_page.py`: The page object model for the integrated page, containing methods to interact with the integrations.
- `e2e/utils/config_loader.py`: Utility functions to load configuration and login data.

## Running the Test

To run the delete integration test, use the following command:

```bash
pytest e2e/tests/integrations/delete_inegration_test.py