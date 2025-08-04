from behave import context
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(context.driver, 20)
#-----------------------------------------XPATH OF ELEMENTS---------------------------------------------------

ticket_module = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Ticket ')]")))

notification_list = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//aside[1]//nav/ul/li/ul/li/a/span[contains(text(), 'Notification Dashboard')]")))

# view_button = context.wait.until(ec.element_to_be_clickable\
#     ((By.XPATH, "(//button[normalize-space(text())='View']/ancestor::*//span[normalize-space(text())='N/A'])[1]")))
view_button = context.wait.until(EC.element_to_be_clickable\
                        ((By.XPATH, "(//app-notification-management//button[text()=' View '])[1]")))

snooze_time = context.wait.until(EC.presence_of_element_located((By.ID, "snoozeTime")))

acknowledge_btn = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Acknowledge ']")))