Feature: Test the functionality of project management module

    @login_required
    Scenario: Test the functionality of basic details page
        Given Navigate to project management page and click on add project button
        When User directly clicked on save button without filling any input field
        Then Error message should be apppeared on all the input fields