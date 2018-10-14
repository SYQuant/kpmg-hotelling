import datetime
import time #used for sleep codes to enable delay between execution of code
# import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Inputs
StartTime = "9:00 AM"
EndTime = "5:00 PM"
Floor = "40"
# Workstation_1 = "40036B"
# Workstation_2 = "40153B"

# Function used to calculate the 3rd business day for earliest booking
def date_by_adding_business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

future_date = str(date_by_adding_business_days(datetime.date.today(),3))
future_date_adjusted = datetime.datetime.strptime(future_date,'%Y-%m-%d').strftime("%m/%d/%Y %a")

# Connect to Python using selenium API and access KPMG website
browser = webdriver.Chrome("C:\\Users\\stephenyao\\Documents\\chromedriver.exe")
browser.get("https://ems.ca.kworld.kpmg.com/VirtualEms/RoomRequest.aspx?data=ity3Dem%2byxxGFZTQvNr97wLAGVQekE8O")

# To maximize screen, use below code
# browser.maximize_window()
# actions = ActionChains(browser)

# Script to fill in various user inputs
browser.find_element_by_name("ctl00$pc$BookDate$box").clear()
browser.find_element_by_name("ctl00$pc$BookDate$box").send_keys(future_date_adjusted)#Date
browser.find_element_by_name("ctl00$pc$StartTime$box").clear()
browser.find_element_by_name("ctl00$pc$StartTime$box").send_keys(StartTime)#Start time
browser.find_element_by_name("ctl00$pc$EndTime$box").clear()
browser.find_element_by_name("ctl00$pc$EndTime$box").send_keys(EndTime)#End time
browser.find_element_by_name("ctl00$pc$Floors$ddl").send_keys(Floor) #Floor Availability
# Access search feature
browser.find_element_by_name("ctl00$pc$GetData").click()
time.sleep(1)

# Books first seat
try:
    element1 = browser.find_element_by_xpath(
        "//img[@alt='Click to add Toronto - BAC - 40074A Workstation to your selected locations']"
    )
    browser.execute_script("arguments[0].scrollIntoView()",element1)
    element1.click()
    print("Your main seat is booked.")
except:
    print("Your main seat is not booked. Now trying for second seat.")
    pass
time.sleep(1)

# Books second seat
try:
    element2 = browser.find_element_by_xpath(
        "//img[@alt='Click to add Toronto - BAC - 40153B Workstation to your selected locations']"
    )
    browser.execute_script("arguments[0].scrollIntoView()",element2)
    element2.click()
    print("Your backup seat is booked.")
except:
    print("No available seats.")
    pass
time.sleep(1)

# Submit reservations to be made
try:
    browser.find_element_by_name("ctl00$pc$submitReservation").click()
except:
    pass
time.sleep(1)
browser.quit()
