Feature: Test the login functionality of GenSOM ERP

    Scenario: Login using valid credentials
        Given User navigate to the website
        When User enter vaild credentials
        And Click on login button
        Then User successfully logged in and navigate to dashboard page of GenSOM ERP

    Scenario: Login using invalid credentials
        Given User navigate to the website
        When User enter invalid credentials
        And Click on login button
        Then User can not able to logged in and system should display the toaster message

    Scenario: Login using without any credentails
        Given User navigate to the website
        When User doesnot enter any credentails
        And Click on login button
        Then Login button should be disabled