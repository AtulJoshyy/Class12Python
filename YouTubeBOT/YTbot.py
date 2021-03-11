import time
import random
from selenium import webdriver

driver = webdriver.Firefox ('G:\Python\instabit')

videos = ['https://www.youtube.com/watch?v=lK-KBkIasJY',
'https://www.youtube.com/watch?v=r_R5a69sPXY','https://www.youtube.com/watch?v=X3K5QBsmEJs']

sleep_time = 0

for i in range(1000):
    print("Watching for {} time".format(i))
    random_video = random.randint(0,2)
    driver.get(videos[random_video])
    time.sleep(sleep_time) # Let the user actually see something!
    sleep_time = random.randint(60, 130)

    time.sleep(5) # Let the user actually see something!
driver.quit() 