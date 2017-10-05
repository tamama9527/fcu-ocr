# -*- coding: UTF-8 -*-
from PIL import Image,ImageEnhance,ImageFilter
import requests
from  pytesseract import *
import io
s=requests.session()
total=1
success=1
while(True):
  r=s.get('https://course.fcu.edu.tw/validateCode.aspx')
  code = r.cookies.get('CheckCode')
  image_file = io.BytesIO(r.content)
  im = Image.open(image_file)
  im = im.point(lambda x: 0 if x<120 else 255)
  im = im.filter(ImageFilter.DETAIL)
  im = im.convert('L')
  im = im.crop((6, 5, 41, 17))
  imageNew = Image.open("0.png")
  imageNew.paste(im,(6,5))
  imageNew.save("decode.png")
  ocr_code=image_to_string(imageNew)
  ocr_code=ocr_code.replace(" ","")
  if code == ocr_code :
  	success+=1
  	total+=1
  else:
  	total+=1
  print str(code)+"   "+str(ocr_code)
  print(u"總次數:"+str(total)+u"  成功次數:"+str(success)+u"成功率:"+str((float(success))/(float(total))*100))