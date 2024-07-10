# # Tutorial 1: First Steps
# # https://behave.github.io/behave.example/tutorials/tutorial01.html
# file:features/tutorial01_basics.feature
# The following feature file provides a simple feature with one scenario
# in the known Given ... When ... Then ... language style (BDD).

Feature: Showing off behave (tutorial01)

Scenario: Run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!