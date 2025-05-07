# Facebook Feed Test

This test file, `fb_feed_test.py`, is designed to verify the functionality of the Facebook feed feature in the application. The test is implemented using the Playwright and Pytest frameworks, and it includes steps to log in to the application, navigate to the Facebook feed, send a message, send an emoji, upload images, send a saved reply, and send a private reply.

## Test Steps

1. **Log in to the application:**
   - The test starts by logging in to the application using the credentials provided in the configuration files.

2. **Load configuration and navigate to Facebook feed:**
   - The test loads the configuration settings and navigates to the Facebook feed page.

3. **Verify comment section URL and send message:**
   - The test verifies that the comment section URL is correct.
   - It sends a message "Good day from jubair ahmed khan tonmoy" in the comment section.
   - The page is scrolled to the bottom to ensure the message is visible.

4. **Send emoji and verify delivery:**
   - The test sends an emoji in the comment section and verifies its delivery.

5. **Send attachments and verify delivery:**
   - The test uploads various images to the comment section:
     - Images (2MB and 6MB)

6. **Send saved reply and verify delivery:**
   - The test sends a saved reply in the comment section and verifies its delivery.

7. **Send private reply:**
   - The test sends a private reply "Dear, this is a private reply" in the comment section.

8. **Attach screenshot:**
   - A screenshot of the page is taken and attached to the test report for verification.

## File Structure

- `e2e/tests/inbox/fb_feed_test.py`: The main test file containing the Facebook feed test.
- `e2e/pages/inbox/fb_feed_page.py`: The page object model for the Facebook feed page, containing methods to interact with the Facebook feed.
- `e2e/utils/config_loader.py`: Utility functions to load configuration and login data.

## Running the Test

To run the Facebook feed test, use the following command:

```bash
pytest e2e/tests/inbox/fb_feed_test.py
```