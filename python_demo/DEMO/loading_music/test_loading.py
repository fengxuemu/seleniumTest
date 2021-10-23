from appium import webdriver
from time import *
#手机配置信息
caps = {
    "platformName":"Android",
    "deviceName":"MuMu",
    "appPackage":"com.netease.cloudmusic",
    "appActivity":".activity.LoadingActivity",
    "noReset":False
}
#打开网易云音乐
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)
#点击登录/注册
driver.find_element_by_id("com.netease.cloudmusic:id/lw").click()
#点击手机登录
driver.find_element_by_id("com.netease.cloudmusic:id/ov").click()
#手机号码输入框输入手机号码
driver.find_element_by_id('com.netease.cloudmusic:id/ho').send_keys('13528712434')
#密码输入框输入密码
driver.find_element_by_id('com.netease.cloudmusic:id/hm').send_keys('fxm1340314113')
#点击登录按钮
driver.find_element_by_id('com.netease.cloudmusic:id/ov').click()

sleep(3)
driver.quit()