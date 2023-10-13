from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
import subprocess

try:
    driver = webdriver.Chrome()

    username = "your username"
    password = "your password"
    driver.get("https://netaccess.iitm.ac.in/account/login")

    user = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[1]/input")
    user.send_keys(username)
    pwd = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[2]/input")
    pwd.send_keys(password)
    submit = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[3]/button")
    submit.click()

    approve_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/a/span")
    approve_button.click()

    listitem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/label")
    listitem.click()

    authorize_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[4]/button")
    authorize_button.click()


    driver.quit()


    successmessage = "message_after_success.vbs"

    subprocess.call(['cscript', successmessage], shell=True)
except:
    
    failmessage = "message_after_failure.vbs"

    subprocess.call(['cscript', failmessage], shell=True)


