import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


@given(u'User logged in and redirect to Make module')
def step_impl(context):
    side_bar = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@aria-label='sidebar']")))
    context.actions.move_to_element(side_bar).click().perform()
    
    master_menu = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//ng-scrollbar//span[text()='Master ']")))
    context.actions.move_to_element(master_menu).click().perform()

    make_menu = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//ng-scrollbar//span[text()='Make']")))
    context.actions.move_to_element(make_menu).click().perform()


@when(u'User click on Add Make button and enter the "{make}" in the input field')
def step_impl(context, make):
    add_button = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']")))
    context.actions.move_to_element(add_button).click().perform()
    
    context.driver.find_element(By.XPATH, "//input[@formcontrolname='make_name']").send_keys(make)
    

@when(u'User click on Submit button then toster message should displayed')
def step_impl(context):
    save = context.wait.until(ec.element_to_be_clickable((By.XPATH,"//button[text()='Save']")))
    time.sleep(0.5)
    context.actions.move_to_element(save).click().perform()
    
    toaster = context.wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='toast-container']")))
    print(toaster.text)
    toaster.click()


@when(u'Entered "{make}" should be displayed on the table')
def step_impl(context, make):
    displayd_make = context.wait.until(ec.presence_of_element_located\
                                ((By.XPATH, f"//ngb-highlight[normalize-space(text())='{make}']"))).text
    
    assert displayd_make == make, f"'{make}' not found in the table."


@then(u'User click on edit icon of added "{make}" and enter new "{updated_make}" in the input field')
def step_impl(context, make, updated_make):
    edit_icon = context.wait.until(ec.element_to_be_clickable\
                        ((By.XPATH, f"//table/tbody/tr[td[normalize-space()='{make}']]/td/a[2]")))
    time.sleep(0.5)
    context.actions.move_to_element(edit_icon).click().perform()
    
    make_input = context.driver.find_element(By.XPATH, "//input[@formcontrolname='make_name']")
    time.sleep(0.5)
    make_input.clear()
    make_input.send_keys(updated_make)
    
    update = context.wait.until(ec.element_to_be_clickable((By.XPATH,"//button[text()='Update']")))
    time.sleep(0.5)
    context.actions.move_to_element(update).click().perform()
    

@then(u'User click on update button then toaster message should displayed')
def step_impl(context):
    toaster = context.wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='toast-container']")))
    print(toaster.text)
    toaster.click()


@then(u'Updated "{updated_make}" should be displayed on the table')
def step_impl(context, updated_make):
    displayd_upd_make = context.wait.until(ec.presence_of_element_located\
                                ((By.XPATH, f"//ngb-highlight[normalize-space(text())='{updated_make}']"))).text
    
    assert displayd_upd_make == updated_make, f"'{updated_make}' not found in the table."


@then(u'User click on delete icon of "{updated_make}" and confirms the action')
def step_impl(context, updated_make):
    delete_icon = context.wait.until(ec.element_to_be_clickable\
        ((By.XPATH, f"//table/tbody/tr[td[normalize-space()='{updated_make}']]/td/a[3]")))
    context.actions.move_to_element(delete_icon).click().perform()


@then(u'Make should be deleted, toaster message should be displayed and details should be removed from the table')
def step_impl(context):
    toaster = context.wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='toast-container']")))
    print(toaster.text)
    toaster.click()
    
    

