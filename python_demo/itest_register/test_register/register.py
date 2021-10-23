from selenium import webdriver
from time import *
import random
from PIL import Image
import pytesseract
from PIL import Image
driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/')
driver.maximize_window()
title = driver.title
print(title)
user_nb = ''.join(random.sample('12456789absdefghijk',5))
user_em = user_nb + '@126.com'
#查找邮箱输入框
driver.find_element_by_id('register_email').send_keys(user_em)
#查找用户名框
driver.find_element_by_xpath('//*[@id="register_nickname"]').send_keys('我梦'+user_nb)
#查找密码框
driver.find_element_by_name('password').send_keys('123456789')
#保存验证码图片
driver.save_screenshot('E:/imooc.png')
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
bottom = code_element.size['height'] + top
im = Image.open('E:/imooc.png')
img = im.crop((left,top,right,bottom))
img.save('E:/imooc1.png')
image = Image.open('E:/imooc1.png')
text = pytesseract.image_to_string(image)
driver.find_element_by_id('captcha_code').send_keys(text)
sleep(30)
driver.quit()
