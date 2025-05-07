# Add Integrations Test

This test file, `add_integrations_test.py`, is designed to verify the functionality of the integrations feature in the application. The test is implemented using the Playwright and Pytest frameworks, and it includes steps to log in to the application, navigate to the integrations page, and verify the integration of various e-commerce and channel platforms.

## Test Steps

1. **Log in to the application:**
   - The test starts by logging in to the application using the credentials provided in the configuration files.

2. **Load configuration and navigate to integrations:**
   - The test loads the configuration settings and navigates to the integrations page.

3. **Verify E-COMMERCE integrations:**
   - The test verifies the integration of the following e-commerce platforms:
     - WooCommerce
     - Shopify
     - Zid
   - It also verifies the integration of the Salla platform.

4. **Verify CHANNEL integrations:**
   - The test verifies the integration of the following channel platforms:
     - Facebook Feed
     - Messenger
     - Instagram Feed
     - Instagram Chat
     - WhatsApp
   - It also verifies the integration of the following channels:
     - Email
     - Viber
     - Telegram
     - Line
   - Finally, it verifies the integration of the Live Chat Plugin.

5. **Attach screenshot:**
   - A screenshot of the page is taken and attached to the test report for verification.

## File Structure

- `e2e/tests/integrations/add_integrations_test.py`: The main test file containing the integrations test.
- `e2e/pages/integrations/available_integrations_page.py`: The page object model for the integrations page, containing methods to interact with the integrations.
- `e2e/utils/config_loader.py`: Utility functions to load configuration and login data.

## Running the Test

To run the integrations test, use the following command:

```bash
pytest e2e/tests/integrations/add_integrations_test.py
```