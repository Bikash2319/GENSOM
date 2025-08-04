import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


@given(u'User is logged in and redirected to sub category page')
def step_impl(context):
    side_bar =  context.wait.until(ec.presence_of_element_located((By.XPATH, "//aside[@class='left-sidebar']")))
    side_bar.click()
    
    master_menu = context.wait.until(ec.presence_of_element_located((By.XPATH, "//span[starts-with(text(), 'Master')]")))
    master_menu.click()
    
    sub_cat = context.wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()='Sub Category']")))
    sub_cat.click()


@when(u'User clicks on add sub category button')
def step_impl(context):
    add_sub_cat = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add SubCategory']")))
    add_sub_cat.click()


@then(u'User enter the sub category name "{sub_catgory}"')
def step_impl(context):
    valid_subcat = context.valid.get("sub_category")
    print(valid_subcat)
    
    time.sleep(10)


@then(u'User click on save button and User should see the success message "Sub Category added successfully"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User click on save button and User should see the success message "Sub Category added successfully"')


@then(u'User should able see the sub category "{sub_catgory}" in the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should see the sub category "{sub_catgory}" in the list')


@when(u'User click on the edit button of "{sub_catgory}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User click on the edit button of "sub_catgory"')


@then(u'User should be edit the sub category name to "{updated_sub}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should be edit the sub category name to "updated_sub"')


@when(u'User clicks on save button and User should see the success message "Sub Category updated successfully"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks on save button and User should see the success message "Sub Category updated successfully"')


@then(u'User should see the sub category "{updated_sub}" in the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should see the sub category "updated_sub" in the list')


@when(u'User clicks on delete button for "{updated_sub}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks on delete button for "updated_sub"')


@when(u'User should see the confirmation dialog and confirms the deletion')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User should see the confirmation dialog and confirms the deletion')


@then(u'User should see the success message "Sub Category deleted successfully"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should see the success message "Sub Category deleted successfully"')