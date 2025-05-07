Feature: Agent

    As a user
    I should be able to create and coonect an agent to a channel.


    @create-agent
    Scenario: Create Agent
        Given I am logged in to the application

        When I click on the create agent button
        And Step 1: I create an agent name "API Agent"

        When I click on the save button
        And Step 2: I create 2 API tools

        When I click on the save button
        And Step 3: I send a message "Hello"

        When I click the next button
        And Step 4: I connect the agent to "raven"

        When I click the Goto main page button
        Then I should see agent on the main page
        