from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  
import time

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

## SETTING PATHS
brave_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe' # CHANGE BROWSER PATH FOR YOUR MACHINE
# chrome_location = <YOUR PATH FOR CHROME HERE>
options.binary_location = brave_location # CHANGE TO chrome_location
# dylan_driver = <YOUR PATH FOR chromedriver.exe HERE>
kevin_driver = 'C:/Users/17087/Downloads/chromedriver_win32/chromedriver.exe'
driver_path = kevin_driver # CHANGE DRIVER PATH FOR YOUR MACHINE

# goes to web page
driver = webdriver.Chrome(options = options, executable_path = driver_path)
driver.get('https://www.youtube.com/')

# types query into box
driver.find_element_by_name("search_query").send_keys("despacito")  
time.sleep(3)

# presses the search button
driver.find_element_by_id("search-icon-legacy").send_keys(Keys.ENTER)  
time.sleep(3)
driver.close()