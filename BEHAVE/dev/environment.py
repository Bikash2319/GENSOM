import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# df = pd.read_excel("C:\\Users\\Bikash Chandra Sahoo\\OneDrive\\Desktop\\Automation\\GenSOM Inputs.xlsx", "Credentials")
# credential = df.to_dict(orient="records")
# file_path = "C:\\Users\\Bikash Chandra Sahoo\\OneDrive\\Desktop\\Automation\\GenSOM Inputs.xlx"


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 20)
    context.actions = ActionChains(context.driver)
    # df = pd.read_excel("Excel path", "Sheet Name")
    # context.credential = df.to_dict(orient="records")

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
    

