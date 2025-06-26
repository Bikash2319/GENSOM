from behave import *
import environment


@given(u'User navigate to the website')
def step_impl(context):
    context.driver.get("https://refex.dev.gensomerp.com")


@when(u'User enter vaild credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enter vaild credentials')


@when(u'Click on login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on login button')


@then(u'User successfully logged in and navigate to dashboard page of GenSOM ERP')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User successfully logged in and navigate to dashboard page of GenSOM ERP')


@when(u'User enter invalid credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enter invalid credentials')


@then(u'User can not able to logged in and system should display the toaster message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User can not able to logged in and system should display the toaster message')


@when(u'User doesnot enter any credentails')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User doesnot enter any credentails')


@then(u'Login button should be disabled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Login button should be disabled')