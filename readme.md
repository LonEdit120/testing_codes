# Code Contents
- selenium_test_01.py
    - first test of selenium, searches keyword for youtube title and plays
    - no bigram algorithm yet
- selenium_test_02.py
    - improved version from selenium_test_01.py
    - fixed issue of playing incorrect song when internet is slow
        - adding "?search_query=" in the url instead of normal searching
- selenium_test_03.py
    - queries taiwanese song according to csv file and gets its youtube id
    - effeciency needs to be improved (830 songs takes 24 minute)
- selenium_test_04.py
    - added Beautiful soup in order to get class's href
    - able to get 3 song;s ID at once now
- selenium_test_05.py
    - combination of selenium_test_03.py and selenium_test_04.py
    - now able to get 3 songs' ID at a time instead of 1, while reducing 40% of the origin required time
- bigram_test_01.py
    - bigram doing sorting on taiwanese song list
