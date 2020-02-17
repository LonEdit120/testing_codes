# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome('C:/Python27/Scripts/chromedriver.exe')
wait = WebDriverWait(driver, 10)

presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

### do bigram and get vid_name
vid_name = "浪子回頭"
###

driver.get("https://www.youtube.com/results?search_query=" + str(vid_name))
parser = BeautifulSoup(driver.page_source, "html.parser")
try:
    # songinfo = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[1]
    songinfo0 = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[0]
    songinfo1 = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[1]
    songinfo2 = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[2]
except:
    pass
get_id = re.compile(r'.+\?v=(.{11})')
if songinfo0:
    songlink0 = songinfo0.get('href')
    result0 = get_id.findall(songlink0)
if songinfo1:
    songlink1 = songinfo1.get('href')
    result1 = get_id.findall(songlink1)
if songinfo2:
    songlink2 = songinfo2.get('href')
    result2 = get_id.findall(songlink2)
print(result0)
print(result1)
print(result2)
