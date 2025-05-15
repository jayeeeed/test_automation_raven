Feature: Agent

    As a user
    I should be able to create and connect an agent to a channel.


    @create
    Scenario: Create and connect agent to a channel
        Given I am logged in to the application

        When I create an custom agent Agent1 with description test agent
        And I should able to connect to a channel

        Then I create an custom agent Agent2 with description test agent
        And I should able to connect to previous channel

        Then I should see a warning message and accept it
        And I should able to see both agents on dashboard
        