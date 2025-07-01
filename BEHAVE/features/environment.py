import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from openpyxl import load_workbook

# df = pd.read_excel("C:\\Users\\Bikash Chandra Sahoo\\OneDrive\\Desktop\\Automation\\GenSOM Inputs.xlsx", "Credentials")
# credential = df.to_dict(orient="records")
# file_path = "C:\\Users\\Bikash Chandra Sahoo\\OneDrive\\Desktop\\Automation\\GenSOM Inputs.xlx"


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 20)
    # df = pd.read_excel("C:\\Users\\Bikash Chandra Sahoo\\OneDrive\\Desktop\\Automation\\GenSOM Inputs.xlsx", "Credentials")
    # context.credential = df.to_dict(orient="records")



    if 'login_required' in scenario.tags:
        context.driver.get("https://release.gensom.sharajman.com/login")
        context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']")\
            .send_keys("bikash.sahoo@sharajman.com")
        context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']")\
            .send_keys("Admin1234")
        context.driver.find_element(By.XPATH, "//button[text()='Login ']").click()
        context.wait.until(ec.url_contains('dash'))


def after_scenario(context, scenario):
    context.driver.quit()

