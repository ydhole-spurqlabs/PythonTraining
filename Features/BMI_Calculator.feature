
Feature: Create test cases using Selenium with Python to automate below BMI calculator tests

  @web
  Scenario Outline: Calculating BMI value by passing multiple inputs
#    Given : BMI Calculator Homepage
    When  : You enter the "<Age>"
    And   : Click on "<Gender>"
    And   : Enter "<Height>"
    And   : Enter your "<Weight>"
    And   : Click on Calculate btn
    And   : Verify Result with "<Expected Result>"
#    Then  : Close browser

    Examples:

      | Age | Gender  | Height  | Weight  | Expected Result |
      | 20  | Male    |  180    |  60     | BMI = 18.5 kg/m2|
      | 35  | Female  |  160    |  55     | BMI = 21.5 kg/m2|
      | 50  | Male    |  175    |  65     | BMI = 21.2 kg/m2|
      | 45  | Female  |  150    |  52     | BMI = 23.1 kg/m2|


