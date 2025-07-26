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

@login_required
Scenario Outline: Verify all the functionality of category module
    Given User logged in and redirect to category master
    When User click on Add Category button
    And User enter category name as "<Cat_Name>"
    And User click on Save button
    Then User should see the category "<Cat_Name>" in the list
    When User click on Edit button for "<Cat_Name>"
    And User change category name to "<Updated_Cat>"
    And User click on Update button
    Then User should see the updated category "<Updated_Cat>" in the list
    When User click on the Delete button for "<Updated_Cat>"
    Then User should see confirmation toaster message "Category deleted successfully"
Examples:
        | Cat_Name      | Updated_Cat      |
        | category2     | new category2    |
        | category3     | new category3    |