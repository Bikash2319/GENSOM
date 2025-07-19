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
    # side_bar = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[1]//ng-scrollbar//nav[@class='sidebar-nav']")))
    side_bar = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[1]//ng-scrollbar//div")))
    context.actions.move_to_element(side_bar).click().perform()
    print('Side bar clicked.')
    
    ticket_module = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Ticket ')]")))
    context.actions.move_to_element(ticket_module).click().perform()
    print('Ticket Module clicked.')

@given(u'User click on Notification list page')
def click_on_notification_list(context):
    notification_list = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[1]//nav/ul/li/ul/li/a/span[contains(text(), 'Notification Dashboard')]")))
    context.actions.move_to_element(notification_list).click().perform()
    print('Notification List clicked.')

@when(u'User click on view button displayed of a ticket having status "N/A"')
def click_on_view_button_status_NA(context):
    # view_button = context.wait.until(ec.element_to_be_clickable\
    #     ((By.XPATH, "(//button[normalize-space(text())='View']/ancestor::*//span[normalize-space(text())='N/A'])[1]")))
    view_button = context.wait.until(ec.element_to_be_clickable\
                            ((By.XPATH, "(//app-notification-management//button[text()=' View '])[1]")))
    context.actions.move_to_element(view_button).click().perform()


@then(u'User enter snooze time click on acknowledge button')
def enter_snooze_click_acknowledge(context):
    snooze_time = context.driver.find_element(By.ID, "snoozeTime")
    snooze_time.send_keys("10")
    acknowledge_btn = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()=' Acknowledge ']")))
    context.actions.move_to_element(acknowledge_btn).click().perform()
    print('Acknowledge button clicked.')
