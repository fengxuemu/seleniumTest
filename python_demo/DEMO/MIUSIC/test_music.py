# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from time import *
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "HWEML"
caps["appPackage"] = "com.netease.cloudmusic"
caps["appActivity"] = ".activity.LoadingActivity"
caps["noReset"] = "True"
caps["newCommandTimeout"] = "3600"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)
#创建歌单
driver.find_elements_by_id("com.netease.cloudmusic:id/icon")[2].click()
start_x = 500
start_y = 1500
end_y = 1000
driver.swipe(start_x,start_y,start_x,end_y)
driver.find_element_by_id("com.netease.cloudmusic:id/create").click()
driver.find_element_by_id("com.netease.cloudmusic:id/etPlaylistName").send_keys("my_music")
sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/tvCreatePlayListComplete').click()
sleep(2)
driver.keyevent(4)
#sleep(3)
driver.find_elements_by_id("com.netease.cloudmusic:id/icon")[1].click()
driver.find_elements_by_id('com.netease.cloudmusic:id/portalImage')[0].click()
options = driver.find_elements_by_id('com.netease.cloudmusic:id/actionBtn')[:3]
for option in options:
    option.click()
    driver.find_element_by_xpath('//*[@text="收藏到歌单"]').click()
    driver.find_elements_by_xpath('//*[@text="my_music"]')[0].click()
    sleep(1)
#查看创建的歌单
driver.keyevent(4)
driver.find_elements_by_id("com.netease.cloudmusic:id/icon")[2].click()
#driver.swipe(start_x,start_y,start_x,end_y)
driver.find_element_by_xpath('//*[@text="my_music"]').click()
songs = driver.find_elements_by_id("com.netease.cloudmusic:id/songName")
for song in songs:
    print(song.text)
#删除创建的歌单
sleep(2)
driver.keyevent(4)
driver.find_element_by_id('com.netease.cloudmusic:id/actionContainer').click()
driver.find_element_by_xpath('//*[@text="删除"]').click()
driver.find_element_by_id('com.netease.cloudmusic:id/buttonDefaultPositive').click()
sleep(3)
driver.quit()