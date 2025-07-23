Feature: Test the functionality of Category Module of GenSOM ERP

@login_required
Scenario Outline: Add a category in module and delete it
    Given User logged in and redirect to category master
    When User click on Add Category button
    And User enter category name as "<Category_Name>"
    And User click on Save button
    Then User should see the category "<Category_Name>" in the list
    When User click on Delete button for "<Category_Name>"
    Then User should see confirmation toaster message "Category deleted successfully"

Examples:
        | Category_Name | 
        | category1     |
        | New Device    |
        