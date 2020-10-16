Feature: Test OrangeHRM webpage
  Scenario: Check OrangeHRM log is displayed
 # Keywords: Given, When, Then, And

  Given Launch the browser
   When Open the OHRM homepage
   Then Verify logo presence
    And Close browser