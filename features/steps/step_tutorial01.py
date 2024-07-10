# # Tutorial 1: First Steps
# # https://behave.github.io/behave.example/tutorials/tutorial01.html
# file:features/steps/step_tutorial01.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
"""
To be able to execute the feature file,
you need to provide a thin automation layer that represents the steps in the feature file with Python functions.
These step functions provide the test automation layer (fixture code) that interacts with the system-under-test (SUT).
"""
from behave import given, when, then


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

"""
Run the Feature Test
$ behave features/tutorial01_basics.feature  
"""
