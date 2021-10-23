import yaml
from appium import webdriver
def appium_load():
    stream = open('cs_caps.yaml','r')
    data = yaml.load(stream,Loader = yaml.FullLoader)
    print(data)
    caps = {}
    caps['platformName'] = data['platformName']
    caps['deviceName'] = data['deviceName']
    caps['appPackage'] = data['appPackage']
    caps['appActivity'] = data['appActivity']
    caps['noReset'] = data['noReset']
    driver = webdriver.Remote("http://"+str(data["ip"])+':'+str(data["port"])+"/wd/hub", caps)
    return driver



