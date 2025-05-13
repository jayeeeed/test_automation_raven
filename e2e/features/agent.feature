Feature: Agent

    As a user
    I should be able to create and coonect an agent to a channel.


    @create
    Scenario: Create Agent
        Given I am logged in to the application

        When I create an custom agent "Agent1" with description "test agent"
        And I should able to connect to a channel

        Then I create an custom agent "Agent2" with description "test agent"
        And I should able to connect to previous channel

        Then I should able to see a warning message
        And I should able to connect channel to "Agent2"
        And I should able to see both agents on dashboard
        