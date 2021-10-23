from pytesseract import pytesseract
from selenium import webdriver
from time import *
import random
from PIL import Image
from itest_register.test_register.find_element import FindElement
class RgisterFunction(object):
    def __init__(self,url):
        self.driver = self.get_driver(url)
    #获取driver，并打开浏器
    def get_driver(self,url):
        driver = webdriver.Chrome()
        #driver = webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        return driver
    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    #定位用户信息
    def get_user_element(self,key):
        find_element =  FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_random(self):
        user_unfo = ''.join(random.sample('12456789absdefghijk', 5))
        return user_unfo

    # 获取图片
    def get_image(self,fileName):
        self.driver.save_screenshot(fileName)
        code_element = self.get_user_element('user_code')
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
    def main(self):
        userInfo = self.get_random()
        user_email = self.get_random() + '@126.com'
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',userInfo)
        self.send_user_info('user_password',1111111)
        self.send_user_info('user_code',11111)
        self.get_user_element('user_bnt').click()
        error_code = self.get_user_element('error_code')
        if error_code == None:
            print('注册成功')
        else:
            self.driver.save_screenshot('E:/python_demo/itest_register/test_register/image/error_code.png')
        sleep(30)
        self.driver.quit()
if __name__ == '__main__':
    register_function = RgisterFunction('http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/')
    register_function.main()
