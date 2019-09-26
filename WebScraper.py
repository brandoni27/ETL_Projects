
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import selenium.common.exceptions
import openpyxl

'''

Notes and To-dos

*Throttling can cause false data because the alert prevents the page from refreshing.
*Figure out how to auto fit the length of the list.
*If selenium.common.exceptions.UnexpectedAlertPresentException is triggered, 
 store the last query number and start at that query after a long break.


    Speed: 8 Throttles at 172.
    Speed: 7 Throttles at around 152.

    *Fix 'off by one error' the first in the list should not be 'str'. It should be empty.
    

'''

def AddressCannon():
    '''

    The Address Cannon reads a list of addresses from a xlsx sheet and queries each student's address
    to see where the closest Eastside school is located.

    Speed: 8 Throttles at 172.
    Speed: 7 Throttles at around 152.

    *Fix 'off by one error' the first in the list should not be 'str'. It should be empty.


    '''


    #Speed = number of seconds between queries.
    speed = 7

    #Holds the list of the closest Eastside School to the address.
    east = []

    #Holds IDs to load dictionary, then Dataframe.
    dictionaryIDs = []

    #Holds Addresses to load dictionary, then dataframe
    dictionaryAddress = []

    #Initiator for the while loop.
    x = 0

    while x < 3:

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
            time.sleep(30)
            try:
                east.append(driver.find_element_by_xpath("//*[@id='resultschools']/p").text)
            except selenium.common.exceptions.NoSuchElementException:
                east.append('-----')
        print(x, "  ", AddressList[x], "    ", IDList[x], " ", east[x], "   ", len(east))
        time.sleep(speed)
        dictionaryIDs.append(IDList[x])
        dictionaryAddress.append(AddressList[x])
        driver.find_element_by_name("from").clear()
        x+=1



    dataDictionary = { 'Student ID' : dictionaryIDs, 'Eastside School' : east, 'Address' : dictionaryAddress }

    masterDataFrame = pd.DataFrame(dataDictionary)
    masterDataFrame.to_excel("/Users/Brando/Desktop/Python Code/StudentDataPyDump.xlsx")
    print(masterDataFrame)




'''
Importing the data from the spreadsheet I pulled from PowerSchool
Step 1: Locate the file and store it.
Step 2: Read the WorkBook and store it.
Step 3: Create a DataFrame using only the Student_Number and Address columns.
Step 4: Scan the columns and add them to a list.
'''
#global eastsideDF
#global addressListDF
#global ID_DF

PowerSchoolData = pd.ExcelFile("/Users/Brando/Desktop/Python Code/StudentDataPy.xlsx")
sheet = pd.read_excel(PowerSchoolData)
frame = pd.DataFrame(sheet, columns=['Student_Number','Address'])
AddressList = frame['Address'].tolist()
IDList = frame['Student_Number'].tolist()

#Opening the webpage and targeting the 'from' input bar. Launching the address cannon.
driver = webdriver.Chrome()
baseURL = "https://www.myschoollocation.com/eastsideHSD/"
driver.get(baseURL)
time.sleep(15)
fromBar = driver.find_element_by_name("from")
time.sleep(10)

AddressCannon()
