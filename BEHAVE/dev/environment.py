import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

file_path = "C:\\Automation\\GENSOM\\BEHAVE\\devn\\variables.xlsx"
# df = pd.read_excel("C:\\Automation\\GENSOM\\BEHAVE\\devn\\variables.xlsx", "Credentials")
# credential = df.to_dict(orient="records")


def before_scenario(context, scenario, file_path):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 20)
    context.actions = ActionChains(context.driver)
    
    context.valid_df = pd.read_excel(file_path, "Valid")
    context.valid = context.valid_df.to_dict(orient="records")
    
    context.invalid_df = pd.read_excel(file_path, "Invalid")
    context.invalid = context.invalid.df.to_dict(orient="records")

    if 'login_required' in scenario.tags:
        context.driver.get("https://refex.dev.gensomerp.com/login")
        context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']")\
            .send_keys("bikash.sahoo@sharajman.com")
        context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']")\
            .send_keys("Admin@1234")
        context.driver.find_element(By.XPATH, "//button[text()='Login ']").click()
        context.wait.until(ec.url_contains('dash'))
        print("Login successfull.")
        time.sleep(2)


def after_scenario(context, scenario):
    profile = context.wait.until(ec.element_to_be_clickable((By.XPATH, "(//img[@class='rounded-circle'])[1]")))
    time.sleep(0.5)
    context.actions.move_to_element(profile).click().perform()
    logout = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//header//app-vertical-navigation//a[text() =' Logout']")))
    time.sleep(0.5)
    context.actions.move_to_element(logout).click().perform()
    context.driver.quit()
    

