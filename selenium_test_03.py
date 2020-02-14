# -*- coding: utf-8 -*-
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# read csv file
import csv
with open('./gitignored_files/taiwanese_song_info.csv', 'rb') as data:
# with open('./gitignored_files/song_test.csv', 'rb') as data:
    reader = csv.reader(data)
    song_dictionary = list(reader)
with open('./gitignored_files/taiwanese_song_info_with_youtube_id.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    # variables in case some songs got issues
    songs_cannot_be_found = []
    count = 1
    # run through the list getting youtube id
    for row in song_dictionary:
        if row == song_dictionary[0] :
            # first line (type) of csv, add in youtube_id
            row.append("youtube_id")
            writer.writerow(row)
        else :
            song_name = row[2]
            # search for the song on youtube by song_name
            driver.get("https://www.youtube.com/results?search_query=" + str(song_name))
            # play the video
            count = count + 1
            try :
                wait.until(visible((By.ID, "video-title")))
                driver.find_element_by_id("video-title").click()
                # get youtube id
                youtube_id = driver.current_url.split('=')[1]
                print(str(count) + " : " + song_name + " -> " + youtube_id)
                # add youtube id to list
                row.append(youtube_id)
                # write all info of song including youtube id
                writer.writerow(row)
            except Exception as e:
                print(str(count) + " : " + song_name + " -> No Search Result !!!")
                songs_cannot_be_found.append(count)
print("songs missing search results :")
print(songs_cannot_be_found)
driver.close()
