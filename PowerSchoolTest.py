from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#import system
#import os

# import pandas as pd
# import selenium.common.exceptions
# import openpyxl

#print(os.name)
#print(os.getcwd())
driver = webdriver.Chrome()


def open_powerschool():
    baseURL = "https://lcpa.powerschool.com/admin/pw.html"
    driver.get(baseURL)
    time.sleep(1.5)


def sign_in():
    usernameField = driver.find_element_by_id("fieldUsername")
    usernameField.send_keys("bwashington")
    passwordField = driver.find_element_by_id("fieldPassword")
    passwordField.send_keys("")
    button = driver.find_element_by_id("btnEnter")
    button.send_keys(Keys.RETURN)

def student_information_get():
    fname = input("Enter the Student's first name: ")
    lname = input("Enter the Student's last name: ")
    gradelvl = int(input("Enter the Student's grade level (9 - 12): "))
    password = input("Enter the Student's ID number?")
    p1 = fname[0]
    p2 = lname
    gradYears = { 9: 2023, 10: 2022, 11: 2021, 12: 2020 }
    p3 = gradYears[gradelvl]
    userID = p1+p2+str(p3)
    print("Username: ", userID)
    print("Password: ", password)

def find_student_by_ID():
    time.sleep(2)
    searchBar = driver.find_element_by_id("studentSearchInput")
    #searchBar.send_keys(student_information_get().password)
    searchBar.send_keys('/10175')
    searchBar.send_keys(Keys.RETURN)

def access_accounts():
    time.sleep(2)
    accesslink = (By.XPATH, '//*[@id="std_information"]/li[1]/a')
    print(accesslink[0])
    accesslink[1].click()

def gmail_sign_in():
    time.sleep(1.5)
    gmail_url = "https://www.gmail.com"
    password = ""
    driver.get(gmail_url)
    time.sleep(4)
    gmail_username = driver.find_element_by_id("identifierId")
    gmail_username.send_keys("bwashington@tfhe.org")
    nextButton = driver.find_element_by_id("identifierNext")
    nextButton.send_keys(Keys.RETURN)
    time.sleep(4)
    gmail_password = driver.find_element_by_name("password")
    gmail_password.send_keys(password)
    gmail_password.send_keys(Keys.RETURN)

def admin_add_user():
    time.sleep(3)
    admin_url = "https://admin.google.com/ac/users"
    driver.get(admin_url)
    add_user = driver.find_element_by_xpath(By.XPATH,//*[@id="yDmH0d"]/c-wiz/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div)
    add_user.send_keys(Keys.RETURN)
#"U26fgb O0WRkf oG5Srb HQ8yf C0oVfc LbgMnd"


#open_powerschool()
#sign_in()
#student_information_get()
#find_student_by_ID()
#access_accounts()
gmail_sign_in()
admin_add_user()
