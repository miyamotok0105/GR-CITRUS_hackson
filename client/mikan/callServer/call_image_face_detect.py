# -*- coding:utf-8 -*-
import json
import urllib2
# ファイル名
headers = { 'File-Name' : 'sample.jpg' }
# ファイル本体を取得
with open('img2.jpg', 'rb') as f:
    image = f.read()
req = urllib2.Request(url='http://localhost:8080/image_face_detect', data=image, headers=headers)
response = urllib2.urlopen(req)
# 戻り値を解析
body = response.read()
response.close()
data = json.loads(body)
print(data['result'])
print(data['text'])
