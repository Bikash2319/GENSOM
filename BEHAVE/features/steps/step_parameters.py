# from behave import given, then
# @given(u'While giving two numers')
# def step_impl(context):
#     print("Two number are provided.")


# @given(u'I need the "{format}" value of it')
# def step_impl(context, format):
#     print("function is :{}".format(format))


# @then(u'we should use "{sign}" sign in between it')
# def step_impl(context, sign):
#     print("sign is :{}".format(sign))

from behave import *
@given('I reach office at "{time}" shift')
def step_implpy(context, time):
      print("Shift is: {}".format(time))