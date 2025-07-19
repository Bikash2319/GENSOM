Feature: CM automated ticket process
    @login_required
    Scenario: Ticket acknowledged status
    Given User logged in and redirect to ticket module
    Given User click on Notification list page
    When User click on view button displayed of a ticket having status "N/A"
    Then User enter snooze time click on acknowledge button



    # Scenario: User raise a ticket from Notification list page and successfully close the ticket 
    # When User logged in and redirect to Notification Dashboard page
    # And User click on View button to raise a ticket by clicking raise a ticket button
