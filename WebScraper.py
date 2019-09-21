
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import selenium.common.exceptions

'''
The AddressCannon 20 second throttling method works. 4 seconds is too fast.
Need to figure out how to auto fit the length of the list.

If selenium.common.exceptions.UnexpectedAlertPresentException is triggered, 
store the last query number and start at that query after a break.
..

'''

def AddressCannon():
    '''
    The AddressCannon queries each student's address to see where the closest Eastside school is.

    Speed: 8 Throttle:172
    Speed:

    '''
    #Speed = number of seconds
    speed = 8
    x = 0
    east = [str]

    while x < 1000:

        fromBar.send_keys(AddressList[x])
        fromBar.send_keys(Keys.RETURN)
        time.sleep(speed)
        #print(str(AddressList[x]))
        try:
            east.append(driver.find_element_by_xpath("//*[@id='resultschools']/p").text)
        except selenium.common.exceptions.NoSuchElementException:
            east.append('-----')
        except selenium.common.exceptions.UnexpectedAlertPresentException:
            print("Throttling...")
            time.sleep(60)
            try:
                east.append(driver.find_element_by_xpath("//*[@id='resultschools']/p").text)
            except selenium.common.exceptions.NoSuchElementException:
                east.append('-----')
        print(x, east[x], IDList[x])
        time.sleep(speed)
        driver.find_element_by_name("from").clear()
        x+=1

'''
Importing the data from the spreadsheet I pulled from PowerSchool
Step 1: Locate the file and store it.
Step 2: Read the WorkBook and store it.
Step 3: Create a DataFrame using only the Student_Number and Address columns.
Step 4: Scan the columns and add them to a list.
'''

PowerSchoolData = pd.ExcelFile("/Users/Brando/Desktop/Python Code/StudentDataPy.xlsx")
sheet = pd.read_excel(PowerSchoolData)
frame = pd.DataFrame(sheet, columns=['Student_Number','Address'])
AddressList = frame['Address'].tolist()
IDList = frame['Student_Number'].tolist()

#Opening the webpage and targeting the 'from' input bar. Launching the address cannon.
driver = webdriver.Chrome()
baseURL = "https://www.myschoollocation.com/eastsideHSD/"
driver.get(baseURL)
fromBar = driver.find_element_by_name("from")

AddressCannon()









#fromBar.send_keys("1813 Margaret Street, san jose")
#fromBar.send_keys(Keys.RETURN)


#You must set the number to define the size of the list.
#This should be automated as well.


#schoolResults = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div/div[4]/p').text
#print(schoolResults)
#schoolAddress = driver.find_element_by_id()

