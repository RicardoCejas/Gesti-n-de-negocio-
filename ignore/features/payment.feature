Feature: Payment System for Buyer

  Scenario: Show available payment methods
    Given the buyer is at the checkout page
    When the system shows the available payment methods
    Then the buyer should see a list of available payment methods

  Scenario: Select a valid payment method
    Given the buyer is at the checkout page
    When the buyer selects "Credit Card" as the payment method
    Then the system should confirm that "Credit Card" is selected

  Scenario: Save a payment method for future use
    Given the buyer wants to save a payment method
    When the buyer saves "PayPal" as a payment method
    Then the system should confirm that "PayPal" is saved for future use

  Scenario: Handle invalid payment method
    Given the buyer selects an invalid payment method
    When the buyer tries to confirm the payment
    Then the system should show an error message

  Scenario: Confirm payment
    Given the buyer has selected a valid payment method
    When the buyer confirms the payment
    Then the system should confirm the payment and proceed with the purchase
