Feature: Inbox

    As a user
    I should be able to send messages, attachments and place order for customer.


    @order
    Scenario: Place order
        Given I am logged in to the application

        When I navigate to the inbox
        And I complete the order placement
        
        Then I send the order placement link to customer
        And I should see the order link in the inbox 'https://ecomwaveevent.com/'


    @message
    Scenario Outline: Send message
        Given I am logged in to the application

        When I navigate to the inbox 
        And I send a message <message>

        Then I should see the <message> in the inbox

        Examples:
        | message                     |
        | Automation Starts here...   |
