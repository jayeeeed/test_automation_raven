# Chatbox Test

This test file, `chatbox_test.py`, is designed to verify the functionality of the chatbox feature in the application. The test is implemented using the Playwright and Pytest frameworks, and it includes steps to log in to the application, navigate to the chatbox, send a message, and upload various types of attachments.

## Test Steps

1. **Log in to the application:**
   - The test starts by logging in to the application using the credentials provided in the configuration files.

2. **Load configuration and navigate to chatbox:**
   - The test loads the configuration settings and navigates to the chatbox page.

3. **Apply filters:**
   - The test applies and save filters to the chatbox.

4. **Automation starts here:**
   - The test sends a message "Automation Starts here..." in the chatbox.

5. **Send attachments and verify delivery:**
   - The test uploads various types of attachments to the chatbox:
     - Images (2MB and 6MB)
     - Videos (2MB and 8MB)
     - Audio (1MB)
     - Document (1MB PDF)

6. **Send recording and verify delivery:**
   - The test uploads an audio recording (1MB).

7. **Add product to cart:**
   - The test adds a product to the cart, fills out the order form, places the order, and verifies the order confirmation.

8. **Send saved reply:**
   - The test sends a saved reply in the chatbox.

9. **Send note:**
   - The test sends a note in the chatbox.

10. **Assign ticket:**
    - The test assigns a ticket and deletes the view.

11. **Top bar functionalities:**
    - The test performs various top bar functionalities like copying a link, changing priority, and adding a tag.

12. **Left bar functionalities:**
    - The test performs various left bar functionalities like searching for a ticket, bulk assigning, composing a WhatsApp message, sorting tickets, pinning a ticket, editing attributes, and reopening a ticket.

13. **Automation ends here:**
    - The test sends a message "Automation ends here..." in the chatbox.

## Allure Reporting

The test uses Allure for reporting, including attaching screenshots and logging steps with descriptions.

## Running the Test

To run this test, use the following command:

```bash
pytest e2e/tests/inbox/chatbox_test.py