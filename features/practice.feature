Feature: Try to login with multiple credentials

    Scenario Outline: User try to login with valid and invalid credentials

        Given Navigate to website's login page
        When User enter "<email>" and "<password>"
        Then Check for valid and invalid credentials
        Examples:
            | email                      | password   |
            | bikash.sahoo@sharajman.com | Admin@1234 |
            | bikash.sahoo@email.com     | Admin      |

