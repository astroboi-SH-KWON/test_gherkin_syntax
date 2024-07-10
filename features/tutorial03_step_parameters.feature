# # Tutorial 3: Step Parameters
# # https://behave.github.io/behave.example/tutorials/tutorial03.html
# file:features/tutorial03_step_parameters.feature
# BEST PRACTICE: Put parameters in double-quoted text to make variation-points visible.
#             The test runner output does not have this problem, because it often marks these parameters as bold text.

Feature: Step Parameters (tutorial03)

  Scenario: Blenders
    Given I put "apples" in a blender
    When  I switch the blender on
    Then  it should transform into "apple juice"
