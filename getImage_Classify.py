# coding:utf-8
import requests, Image, random, caffe, shutil, os

labels = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
model_def = "deploy.prototxt"
model_weights = "misustc_iter.caffemodel"
if not os.path.exists("image"):
    os.mkdir("image")
for i in labels:
    if not os.path.exists("image/" + i):
        os.mkdir("image/" + i)
index = 0
url = "http://mis.teach.ustc.edu.cn/randomImage.do?date='" + str(random.randint(0, 2147483647)) + "'"
table = [255 if i > 140 else i for i in xrange(256)]


def getImage():
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
    img.crop((00, 0, 20, 20)).save("image/tmp0.jpg")
    img.crop((20, 0, 40, 20)).save("image/tmp1.jpg")
    img.crop((40, 0, 60, 20)).save("image/tmp2.jpg")
    img.crop((60, 0, 80, 20)).save("image/tmp3.jpg")


def classify():
    global index
    for i in [0, 1, 2, 3]:
        filename = "image/tmp" + str(i) + ".jpg"
        im = caffe.io.load_image(filename, False)
        transformed_image = transformer.preprocess('data', im)
        net.blobs['data'].data[...] = transformed_image
        output = net.forward()
        output_prob = output['prob'][0]
        result = labels[output_prob.argmax()]
        shutil.move(filename, "image/" + result + "/" + str(index) + ".jpg")
        index += 1


if __name__ == "__main__":
    caffe.set_mode_cpu()
    net = caffe.Net(model_def, model_weights, caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))

    while (index < 1000):
        getImage()
        classify()
    os.remove("image/tmp.jpg")
