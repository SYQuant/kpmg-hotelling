
# coding: utf-8

# In[16]:

import datetime
import time #used for sleep codes to enable delay between execution of code
# import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# CHROME_PATH = '/usr/bin/google-chrome'
# CHROMEDRIVER_PATH = 'C:\\Users\\stephenyao\\Documents\\chromedriver.exe'

# CHROME_PATH = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"'
# CHROMEDRIVER_PATH = 'C:\\Users\\stephenyao\\Documents\\chromedriver.exe'

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % "1920,1080")
# chrome_options.binary_location = CHROME_PATH
# chrome_exec_shim = os.environ.get("CHROMEDRIVER_PATH", "CHROMEDRIVER_PATH")


# In[17]:

# inputs
StartTime = "9:00 AM"
EndTime = "5:00 PM"
Floor = "40"
# Workstation_1 = "40036B"
# Workstation_2 = "40153B"


# In[18]:

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


# In[19]:

# Connect to Python using selenium API and access KPMG website
browser = webdriver.Chrome("C:\\Users\\stephenyao\\Documents\\chromedriver.exe")
# browser = webdriver.Ie("C:\\Users\\stephenyao\\Python Projects\\IEDriverServer.exe")
browser.get("https://ems.ca.kworld.kpmg.com/VirtualEms/RoomRequest.aspx?data=ity3Dem%2byxxGFZTQvNr97wLAGVQekE8O")

# To maximize screen, use below code
# browser.maximize_window()
# actions = ActionChains(browser)


# In[20]:

browser.find_element_by_name("ctl00$pc$BookDate$box").clear()
browser.find_element_by_name("ctl00$pc$BookDate$box").send_keys(future_date_adjusted)#Date


# In[21]:

browser.find_element_by_name("ctl00$pc$StartTime$box").clear()
browser.find_element_by_name("ctl00$pc$StartTime$box").send_keys(StartTime)#Start time
browser.find_element_by_name("ctl00$pc$EndTime$box").clear()
browser.find_element_by_name("ctl00$pc$EndTime$box").send_keys(EndTime)#End time


# In[22]:

browser.find_element_by_name("ctl00$pc$Floors$ddl").send_keys(Floor) #Floor Availability


# In[23]:

# Access search feature
browser.find_element_by_name("ctl00$pc$GetData").click()


# In[24]:

time.sleep(1)


# In[25]:

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


# In[26]:

time.sleep(1)


# In[27]:

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


# In[28]:

time.sleep(1)


# In[29]:

# Submit reservations to be made
try:
    browser.find_element_by_name("ctl00$pc$submitReservation").click()
except:
    pass


# In[30]:

time.sleep(1)
browser.quit()


# In[ ]:
