# Feature: Login into the gensom software
#     Scenario: User try to login with valid credentials
#         Given Open the browser and enter the url
#         When user enter the email and password
#         And user click on login button
#         Then user should successfully logged in and dashboard page should be displayed

#     Scenario: User try to login with invalid credentials
#         Given Open the browser and enter the url
#         When user entered the wrong credentials
#         And  user click on login button
#         Then Incorrect username or password toaster message should be displayed to user.

#     Scenario: User try to login without entering credentials
#         Given Open the browser and enter the url
#         When user click on login button without entering credentials
#         Then Login button should be disabled and System should prompt the user to enter email and password
    
#     Scenario: User account locked after three failed login attempts
#         Given Open the browser and enter the url
#         When User click on login button for three times by entering incorrect credentials
#         Then At fourth click user account get locked for an hour and toaster message should be displayed 


