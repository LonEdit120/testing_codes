#! python2.7
# -*- coding: utf-8 -*-
import sys
import time
import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import re

imp.reload(sys)
# sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome('C:/Python27/Scripts/chromedriver.exe')
wait = WebDriverWait(driver, 10)

presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# read csv file
import csv
with open('./gitignored_files/taiwanese_song_info.csv', 'r') as data:
# with open('./gitignored_files/song_info.csv', 'r') as data:
    reader = csv.reader(data)
    song_dictionary = list(reader)
with open('./gitignored_files/taiwanese_song_info_with_youtube_id.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    # variables in case some songs got issues
    songs_cannot_be_found = []
    count = 1
    # run through the list getting youtube id
    for row in song_dictionary:
        if row == song_dictionary[0] :
            # first line (type) of csv : song_name,id1,id2,id3,status
            writer.writerow(["song_name","id1","id2","id3","status"])
        else :
            song_name = row[2]
            # search for the song on youtube by song_name
            driver.get("https://www.youtube.com/results?search_query=" + str(song_name))
            # play the video
            count = count + 1
            try :
                parser = BeautifulSoup(driver.page_source, "html.parser")
                try:
                    # songinfo = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[1]
                    songinfo1 = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[0]
                    songinfo2 = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[1]
                    songinfo3 = parser.findAll(attrs={'class', 'yt-simple-endpoint style-scope ytd-video-renderer'})[2]
                except Exception as e:
                    pass
                get_id = re.compile(r'.+\?v=(.{11})')
                if songinfo1:
                    songlink1 = songinfo1.get('href')
                    result1 = get_id.findall(songlink1)
                    # print(result1[0])
                if songinfo2:
                    songlink2 = songinfo2.get('href')
                    result2 = get_id.findall(songlink2)
                    # print(result2[0])
                if songinfo3:
                    songlink3 = songinfo3.get('href')
                    result3 = get_id.findall(songlink3)
                    # print(result3[0])

                print(str(count) + " : " + song_name + " -> " + result1[0])
                print(str(count) + " : " + song_name + " -> " + result2[0])
                print(str(count) + " : " + song_name + " -> " + result3[0])

                # add youtube id to list
                id1 = result1[0]
                id2 = result2[0]
                id3 = result3[0]
                # write all info of song including youtube id
                writer.writerow([row[2],id1,id2,id3,""])
            except Exception as e:
                print(e)
                print(str(count) + " : " + song_name + " -> No Search Result !!! ")
                writer.writerow(["missing"])
                songs_cannot_be_found.append(count)
print("songs missing search results :")
print(songs_cannot_be_found)
driver.close()
