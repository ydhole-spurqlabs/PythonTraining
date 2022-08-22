from behave import *


use_step_matcher("re")

# @given(": User is on calculator page")
# def step_impl(context):


@when(": User enters following inputs")
def step_impl(context):
    context.calpage.enter_number()


@step(": User click on calculate button")
def step_impl(context):
    context.calpage.calculatebtn_click()


@then(": User verifies the actual result with expected result")
def step_impl(context):
    context.calpage.verify_result()


