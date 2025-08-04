Feature: To test the functionality of sub category module

#     @login_required
#     Scenario Outline: To test the add edit and delete fuctionality of sub category module
#     Given User is logged in and redirected to sub category page
#     When User clicks on add sub category button
#     Then User enter the sub category name "<sub_catgory>"
#     And User click on save button and User should see the success message "Sub Category added successfully"
#     Then User should able see the sub category "<sub_catgory>" in the list
#     When User click on the edit button of "<sub_catgory>"
#     Then User should be edit the sub category name to "<updated_sub>"
#     When User clicks on save button and User should see the success message "Sub Category updated successfully"
#     Then User should see the sub category "<updated_sub" in the list
#     When User clicks on delete button for "<updated_sub>" 
#     When User should see the confirmation dialog and confirms the deletion
#     Then User should see the success message "Sub Category deleted successfully"
# Examples:
#     | sub_category   | updated_sub    |
#     | sub_cat 1      | updated_sub    |
#     | sub_cat 2      | updated_sub_2  |


Scenario: Add, Edit, and Delete Sub Category using data from Excel
    Given User is logged in and redirected to the Sub Category page
    When User fetches sub category test data from the Excel sheet
    And User clicks on the "Add Sub Category" button
    Then User enters sub category name from Excel
    And User clicks on the "Save" button and sees the success message "Sub Category added successfully"
    Then User should see the newly added sub category in the list
    When User clicks on the "Edit" button of the sub category
    Then User updates the sub category name from Excel
    When User clicks on the "Save" button and sees the success message "Sub Category updated successfully"
    Then User should see the updated sub category in the list
    When User clicks on the "Delete" button of the updated sub category
    And User confirms the deletion
    Then User should see the success message "Sub Category deleted successfully"
