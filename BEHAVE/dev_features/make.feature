Feature: Test the functionality of 'Make' module
    
    @login_required
    Scenario Outline: To add, update and delete make
    Given User logged in and redirect to Make module
    When User click on Add Make button and enter the "<make>" in the input field
    And User click on Submit button then toster message should displayed
    And Entered "<make>" should be displayed on the table
    Then User click on edit icon of added "<make>" and enter new "<updated_make>" in the input field
    And User click on update button then toaster message should displayed
    And Updated "<updated_make>" should be displayed on the table
    Then User click on delete icon of "<updated_make>" and confirms the action
    Then Make should be deleted, toaster message should be displayed and details should be removed from the table

    Examples:
    | make    |   updated_make |
    | make1   |   new make 1   |
    | make2   |   new make 2   |





