# Datalab Test

This test file, `datalab_test.py`, is designed to verify the functionality of the datalab feature in the application. The test is implemented using the Playwright and Pytest frameworks, and it includes steps to log in to the application, navigate to the datalab, create a datalab, enter various inputs, and delete the datalab.

## Test Steps

1. **Log in to the application:**
   - The test starts by logging in to the application using the credentials provided in the configuration files.

2. **Load configuration and navigate to datalab:**
   - The test loads the configuration settings and navigates to the datalab page.

3. **Create datalab:**
   - The test creates a new datalab with a title, description, and image.

4. **Enter Text Inputs:**
   - The test enters various text inputs such as first name, description, age, mobile number, email, LinkedIn URL, and purchase date.

5. **Enter Media Inputs:**
   - The test enters media inputs such as profile image, demo video, and attachment file.

6. **Enter Multiple Choice Inputs:**
   - The test enters multiple choice inputs such as favorite colors and gender.

7. **Enter Group Inputs:**
   - The test enters group inputs such as item name and item quantity.

8. **Edit datalab info:**
   - The test edits the datalab information such as title and button text.

9. **Enter into Datalab:**
   - The test navigates into the datalab section.

10. **Download Sample Data:**
    - The test downloads sample data from the datalab.

11. **Create Datalab Entry:**
    - The test creates a new datalab entry with various inputs.

12. **Import data to datalab:**
    - The test imports data to the datalab from a CSV file.

13. **Delete single datalab entry:**
    - The test deletes a single datalab entry.

14. **Delete datalab:**
    - The test deletes the entire datalab.

## File Structure

- `e2e/tests/datalab/datalab_test.py`: The main test file containing the datalab test.
- `e2e/pages/datalab/datalab_page.py`: The page object model for the datalab page, containing methods to interact with the datalab.
- `e2e/utils/config_loader.py`: Utility functions to load configuration and login data.

## Running the Test

To run the datalab test, use the following command:

```bash
pytest e2e/tests/datalab/datalab_test.py