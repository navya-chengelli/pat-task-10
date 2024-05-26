

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC# Setup WebDriver path and options
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Instagram profile
driver.get("https://www.instagram.com/guviofficial/")
wait = WebDriverWait(driver, 10)
#driver.quit()
# Find the followers and following elements using explicit wait
followers_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span/span")))
following_element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button/span/span")))
# Extract the text which contains the number of followers and following
followers_count = followers_element.text  # text for following
following_count = following_element.text  # Text for following
#
print(f"Followers: {followers_count}")
print(f"Following: {following_count}")
#
# Close the browser
driver.quit()