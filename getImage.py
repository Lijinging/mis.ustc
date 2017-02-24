# coding:utf-8
import requests, Image

url = "http://mis.teach.ustc.edu.cn/randomImage.do?date='1487753436647'"
count = 25
table = [0 if i < 120 else i for i in xrange(256)]
for i in xrange(count):
    req = requests.get(url)
    try:
        with open("image/tmp.jpg", 'wb') as file:
            file.write(req.content)
    except IOError:
        print "IOError"
    finally:
        file.close()
    req.close()
    img = Image.open("image/tmp.jpg").convert('L').point(table)
    img.crop((0, 0, 20, 20)).save("image/" + str(i * 4 + 0) + ".jpg")
    img.crop((20, 0, 40, 20)).save("image/" + str(i * 4 + 1) + ".jpg")
    img.crop((40, 0, 60, 20)).save("image/" + str(i * 4 + 2) + ".jpg")
    img.crop((60, 0, 80, 20)).save("image/" + str(i * 4 + 3) + ".jpg")
