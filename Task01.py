from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pytest
#from webdriver_manager.chrome import ChromeDriverManager 

    
print("Hello OpenNet")
# Setting up the Chrome mobile emulator
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=360,640")  # Setting mobile viewport size
chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})  # Choosing iPhone X as the device

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
#Maximise the window size
driver.maximize_window()  

# Step 1 : To go on given url 
url = "https://m.twitch.tv/"
driver.get(url)
# Wait for the page to load
time.sleep(5)

# Step 2 : click in the search icon
search_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@href = '/search']")))
search_icon.click()

# Step 3 : Input "StarCraft II" into the search field
search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@placeholder= 'Search...']")))
search_field.send_keys("StarCraft II")
search_field.send_keys(Keys.ENTER)
print("user enter after entering details in Search ")


# Step 4 : Scroll the page 2 times
for scroll in range(2):
    # Perform scrolling using ActionChains
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).perform()
    print(f"user scrolled {(scroll + 1)} time")
    time.sleep(2)  # Wait for the content to load

print("user scrolled 2 times completed")

# Step 5: To click on Any Streamer
any_one_streamer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'StarCraft II')]/..")))
any_one_streamer.click()
print("clicked on Any Streamer")
time.sleep(5)

# Capture the current time in Epoch format
current_time_epoch = str(int(time.time()))

# Create a folder with the name "Screenshot_currentDate"
folder_name = "Screenshot"
os.makedirs(folder_name, exist_ok=True)

# Capture the current time in Epoch format
current_time_epoch = str(int(time.time()))

# Create a folder with the name "Screenshot_currentDate" current_time_epoch + ".png"
folder_name = "Screenshot"
file_name = current_time_epoch + ".png"
os.makedirs(folder_name, exist_ok=True)

# Take a screenshot of the streamer page and store it in the folder
screenshot_path = os.path.join(folder_name, file_name)
driver.save_screenshot(screenshot_path)
print("Screenshot is caputured and Saved in Screenshot Folder")


driver.quit()


