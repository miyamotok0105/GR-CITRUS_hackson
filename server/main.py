# -*- coding: utf-8 -*-
#-d "name=John Doe"
#curl -i http://127.0.0.1:8000/vehicle/12345678

#curl -X POST -i http://127.0.0.1:8000/helloResource -d "name=John Doe"

# -*- coding:utf-8 -*-
import cv2
import sys
import json
import falcon
from PIL import Image
import base64
#from StringIO import StringIO
from io import StringIO

import random

app = falcon.API()

class HelloResource(object):
    
    # postされた時の動作
    def on_post(self, req, res):
        
        # postパラメーターを取得
        body = req.stream.read()
        data = json.loads(body)
        
        # パラメーターの取得
        name = data['name']
        
        msg = {
            "message": "Hello, " + name
        }
        res.body = json.dumps(msg)

class ImageSample(object):
    
    # postされた時の動作
    def on_post(self, req, res):
        
        # headerからファイル名を取得
        filename = req.get_header('File-Name')
        
        # bodyから画像ファイルのバイナリ取得
        body = req.stream.read()
        
        # ファイルを保存
        with open(filename, 'wb') as f:
            f.write(body)
        
        res.body = json.dumps({'result':'ok'})


class ImageFaceDetect(object):
    
    # postされた時の動作
    def on_post(self, req, res):
        
        # headerからファイル名を取得
        filename = req.get_header('File-Name')
        
        # bodyから画像ファイルのバイナリ取得
        body = req.stream.read()
        
        # ファイルを保存
        with open(filename, 'wb') as f:
            f.write(body)
        
        text = self.face_detect(filename)
        
        res.body = json.dumps({'result':'ok', 'text' : text})

    def face_detect(self, filename):
        img = cv2.imread(filename)

        cascPath = "haarcascade_frontalface_alt.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # Draw a rectangle around the faces                                                                                                 
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print("face hit!!!")
            print(x, ":",y, ":", x+w, ":", y+h)
            return "face hit!!! " + str(x), ":",str(y), ":", str(x+w), ":", str(y+h)

        if len(faces) == 0:
            print("face is not hit")
            return "face is not hit"
        return ""


class ImageResource(object):
    
    def readb64(base64_string):
        sbuf = StringIO()
        sbuf.write(base64.b64decode(base64_string))
        pimg = Image.open(sbuf)
        return pimg

    # postされた時の動作
    def on_post(self, req, res):
        
        print("1")
        # postパラメーターを取得
        body = req.stream.read()
        #print(body)
        print("2")
        #data = json.loads(body.decode('utf-8'))
        data = json.loads(body.decode('utf-8'))

        print("3")
        # パラメーターの取得
        image = data['image']
        #print(len(res_font))
        
        res.body = "yeahhhhh!!!!!"


app = falcon.API()
app.add_route("/hello", HelloResource())
app.add_route("/image", ImageResource())
app.add_route("/image_sample", ImageSample())
app.add_route("/image_face_detect", ImageFaceDetect())



if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8080, app)
    httpd.serve_forever()
