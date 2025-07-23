import time
from behave import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

@given(u'User logged in and redirect to ticket module')
def redirect_and_navigate(context):

    context.actions.move_to_element(context.side_bar).click().perform()
    print('Side bar clicked.')
    context.actions.move_to_element(context.ticket_module).click().perform()
    print('Ticket Module clicked.')

@given(u'User click on Notification list page')
def click_on_notification_list(context):
    
    context.actions.move_to_element(context.notification_list).click().perform()
    print('Notification List clicked.')

@when(u'User click on view button displayed of a ticket having status "N/A"')
def click_on_view_button_status_NA(context):

    context.actions.move_to_element(context.view_button).click().perform()


@then(u'User enter snooze time click on acknowledge button')
def enter_snooze_click_acknowledge(context):
    
    context.snooze_time.send_keys("10")
    context.actions.move_to_element(context.acknowledge_btn).click().perform()
    print('Acknowledge button clicked.')
