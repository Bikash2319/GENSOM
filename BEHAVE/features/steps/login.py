# import time
# from behave import *
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.wait import WebDriverWait


# @given(u'Open the browser and enter the url')
# def redirect(context):
#     context.driver.get("https://release.gensom.sharajman.com/login")


# @when(u'user enter the email and password')
# def login_using_correct_credentials(context):
#     context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']").send_keys("bikash.sahoo@sharajman.com")
#     context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("Admin@1234")

# @when(u'user click on login button')
# def login_button(context):
#     context.driver.find_element(By.XPATH, "//button[text()='Login ']").click()
#     time.sleep(1)

# @then(u'user should successfully logged in and dashboard page should be displayed')
# def get_url(context):
#     time.sleep(3)
#     current_url = context.driver.current_url
#     assert 'dash' in current_url, "Dashboard page is not displayed."

# @when(u'user entered the wrong credentials')
# def login_using_incorrect_credentials(context):
#     context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']").send_keys("bikash@sharajman.com")
#     context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("123456ASDFG")

# @then(u'Incorrect username or password toaster message should be displayed to user.')
# def incorrect_credentials_toaster(context):
#     time.sleep(2)
#     toaster = context.driver.find_element(By.XPATH, "//div[@id='toast-container']")
#     toaster_message = toaster.text
#     assert toaster_message == "Incorrect username or password", "Toaster message does not matched."

# @when(u'user click on login button without entering credentials')
# def no_credentials(context):
#     time.sleep(1)
#     email_field = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
#     email_field.send_keys("")
#     time.sleep(1)
#     password_field = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='password']")))
#     password_field.send_keys("")
#     time.sleep(1)


# @then(u'Login button should be disabled and System should prompt the user to enter email and password')
# def input_field_error_message(context):

#     email_error_text = context.driver.find_element(By.XPATH, "//label[text() = 'Email Address']/following-sibling::*//span[text() = 'Email is required']").text
#     assert 'Email is required' in email_error_text, "Error message is not displaying under email"

#     # password_error_text = context.driver.find_element(By.XPATH, "//label[text() = 'Password']/following-sibling::*//span[text() = 'Password is required']").text
#     # assert 'Password is required' in password_error_text, "Error message is not displaying under password"

#     login_btn = context.driver.find_element(By.XPATH, "//button[text() = 'Login ']")
#     assert not login_btn.is_enabled(), "Login button is disabled, if credentials are not provided before clicking login button."

# @when(u'User click on login button for three times by entering incorrect credentials')
# def click_login_button_three_times(context):
#     login_btn = context.driver.find_element(By.XPATH, "//button[text() = 'Login ']")
#     toaster = context.wait.until(ec.visibility_of_element_located((By. ID, "toast-container")))
    
#     email_field = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
#     email_field.send_keys("bikash.sahoo@gamil.com")
#     time.sleep(1)
#     password_field = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='password']")))
#     password_field.send_keys("nopassword")
#     time.sleep(1)
    
#     for i in range(2):
#         login_btn.click()
#         print(f"Login click {i} done.")
#         print(f"Toaster message : {toaster}")
#         time.sleep(1)
    
# @then(u'At fourth click user account get locked for an hour and toaster message should be displayed')
# def click_fourth_time_on_login(context):
#     login_button.click()
#     toaster = context.wait.until(ec.visibility_of_element_located((By. ID, "toast-container")))
#     toaster_text = toaster.text
#     print(f"Toaster message is : {toaster_text}")
    