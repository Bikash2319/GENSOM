import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@given(u'Navigate to project management page and click on add project button')
def nav_project(context):
    print("1")
    context.driver.get("https://release.gensom.sharajman.com/plant-management")
    print("2")
    add_project_button = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Project']")))
    add_project_button.click()
        

@when(u'User directly clicked on save button without filling any input field')
def click_save_without_any_details(context):
    print("4")
    save_button = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']")))
    save_button.click()


@then(u'Error message should be apppeared on all the input fields')
def errro_message_on_input_fields(context):
    time.sleep(1)
    print("6")
    error_messages = context.driver.find_elements(By.XPATH, "//div[@class='cst-input-error']//span")
    print("7")
    count= len(error_messages)
    print(f"Save button is clicked, total {count} no of errror messages are appeared.")
    
