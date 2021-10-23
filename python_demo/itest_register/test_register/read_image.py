import pytesseract
from PIL import Image
#image = Image.open('E:/imooc1.png')
#text = pytesseract.image_to_string(image)
#print(text)


from ShowapiRequest import ShowapiRequest
r = ShowapiRequest("http://route.showapi.com/1274-2","779922","2d482b112a1e406493662ec93a732c25" )
r.addBodyPara("imgUrl", "https://showapi.oss-cn-hangzhou.aliyuncs.com/site/apiCase/1274/20210709160926.png")
r.addBodyPara("base64", "")
res = r.post()
print(res.text) # 返回信息

