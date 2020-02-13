import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver.maximize_window()
driver.get("https://www.youtube.com")

wait = WebDriverWait(driver, 10)

presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

### do bigram and get vid_name
vid_name = "nightcore"
###

# Search for the video.
time.sleep(1)
wait.until(visible((By.NAME, "search_query")))
#click search bar
driver.find_element_by_name("search_query").click()
#send in vid name
driver.find_element_by_name("search_query").send_keys(vid_name)
#click search icon
driver.find_element_by_id("search-icon-legacy").click()

# Play the video.
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()
