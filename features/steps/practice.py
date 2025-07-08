from behave import *


@given(u'Navigate to website\'s login page')
def step_impl(context):
    print("Navigated")

@when(u'User enter "{email}" and "{password}"')
def step_impl(context, email, password):
    print("email".format(email))
    print("password".format(password))

@then(u'Check for valid and invalid credentials')
def step_impl(context):
    print("login jfiej")


