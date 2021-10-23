from DEMO.loading_music.config import loading_cs as ls
from time import *
d = ls.appium_load()
d.implicitly_wait(3)
#ls.send(d,"com.netease.cloudmusic:id/ho",13528712434)
#ls.send(d,"com.netease.cloudmusic:id/hm","fxm1340314113")
#ls.find(d,"com.netease.cloudmusic:id/ov")
#点击登录/注册
d.find_element_by_id("com.netease.cloudmusic:id/lw").click()
#点击手机登录
d.find_element_by_id("com.netease.cloudmusic:id/ov").click()
#手机号码输入框输入手机号码
d.find_element_by_id('com.netease.cloudmusic:id/ho').send_keys('13528712434')
#密码输入框输入密码
d.find_element_by_id('com.netease.cloudmusic:id/hm').send_keys('fxm1340314113')
#点击登录按钮
d.find_element_by_id('com.netease.cloudmusic:id/ov').click()

sleep(3)
d.quit()

