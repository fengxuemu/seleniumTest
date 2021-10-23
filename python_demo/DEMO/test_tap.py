# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "MuMu"
caps["appPackage"] = "com.mumu.launcher"
caps["appActivity"] = ".Launcher"
caps["noReset"] = "True"
caps["newCommandTimeout"] = "3600"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#x1 = 79.00
#y1 = 180.00
#x2 = 540.00
#y2 = 960.00
#x_1 = x1/x2
#y_1 = y1/y2
#x = driver.get_window_size()['width']
#y = driver.get_window_size()['height']
#print(x,y)
#print(x_1*x,y_1*y)
#driver.tap([(x_1*x,y_1*y)])
driver.tap([(79,180)])

time.sleep(30)
driver.quit()