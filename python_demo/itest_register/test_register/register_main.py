#coding = utf-8
from pytesseract import pytesseract
from selenium import webdriver
from time import *
import random
from PIL import Image
driver = webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.get('http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    sleep(5)
#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element
#获取随机数
def get_random():
    user_unfo = ''.join(random.sample('12456789absdefghijk',5))
    return user_unfo

#获取图片
def get_image(fileName):
    driver.save_screenshot(fileName)
    code_element = driver.find_element_by_id('getcode_num')
    print(code_element.location)
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    bottom = code_element.size['height'] + top
    im = Image.open(fileName)
    img = im.crop((left, top, right, bottom))
    img.save(fileName)

def get_image_code(fileName):
    image = Image.open(fileName)
    text = pytesseract.image_to_string(image)
    return text

def test_main():
    userInfo  = get_random()
    user_email = get_random() + '@126.com'
    driver_init()
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(userInfo)
    get_element('register_password').send_keys('11111111')
    get_element('captcha_code').send_keys('11111')
    get_element('register-btn').click()

    sleep(30)
    driver.close()

test_main()

