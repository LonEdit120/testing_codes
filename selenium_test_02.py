# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

### do bigram and get vid_name
vid_name = "浪子回頭"
###

driver.get("https://www.youtube.com/results?search_query=" + str(vid_name))

# Play the video.
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()
