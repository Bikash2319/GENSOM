import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By 


@given(u'User logged in and redirect to category master')
def step_impl(context):
    
    side_bar = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@aria-label='sidebar']")))
    context.actions.move_to_element(side_bar).click().perform()

    master_menu = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//ng-scrollbar//span[text()='Master ']")))
    context.actions.move_to_element(master_menu).click().perform()

    category_menu = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//ng-scrollbar//span[text()='Category']")))
    context.actions.move_to_element(category_menu).click().perform()
    


@when(u'User click on Add Category button')
def step_impl(context):
    add_button = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Category']")))
    context.actions.move_to_element(add_button).click().perform()
    print('Add Category button clicked.')


@when(u'User enter category name as "{Category_Name}"')
def step_impl(context, Category_Name):
    category_input = context.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='catType']")))
    category_input.send_keys(Category_Name)
    

@when(u'User click on Save button')
def step_impl(context):
    #save_button = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
    save_button = context.driver.find_element(By.XPATH, "//button[text()='Save']")
    time.sleep(1)
    context.actions.move_to_element(save_button).click().perform()
    print('Save button clicked.')


@then(u'User should see the category "{Category_Name}" in the list')
def step_impl(context, Category_Name):
    cat_element = context.wait.until(ec.presence_of_element_located((By.XPATH, f"//ngb-highlight[normalize-space(text())='{Category_Name}']"))).text
    assert cat_element == Category_Name, f"Expected category '{Category_Name}' not found in the list."    


@when(u'User click on Delete button for "{Category_Name}"')
def step_impl(context, Category_Name):
    delete_icon = context.wait.until(ec.element_to_be_clickable((By.XPATH, f"//table/tbody/tr[td[normalize-space()='{Category_Name}']]/td/a[3]")))
    context.actions.move_to_element(delete_icon).click().perform()
    
    confirm_yes = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Yes']")))
    time.sleep(0.5)
    context.actions.move_to_element(confirm_yes).click().perform()
    print(f'Delete button clicked for category: {Category_Name}')


@then(u'User should see confirmation toaster message "Category deleted successfully"')
def step_impl(context):
    toater_mesage = context.wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='toast-container']"))).text
    assert "Category deleted successfully" in toater_mesage, "Toaster message not displayed as expected."
    print("Category deleted successfully toaster message displayed.")