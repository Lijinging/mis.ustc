# coding:utf-8

import os
import scipy.io as sio
import numpy
import Image


def function(dirname, filename, matname):
    record = {}
    s = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
    for dir in os.listdir(dirname):
        if os.path.isdir(dirname + dir):
            l = os.listdir(dirname + dir)
            for i in l:
                record[int(i[:-4])] = dir
    f = open(filename, "w")
    for i in record:
        f.write(record[i] + "\\" + str(i) + ".jpg " + str(s.index(record[i])) + "\n")
    f.close()

    # 以下创建mat文件
    label = numpy.zeros((0, 1), dtype="uint8")
    data = numpy.zeros((0, 400), dtype="int")
    f = open(filename, "r")
    while True:
        line = f.readline()
        if line == '':
            break
        tmp = line.split()
        img = numpy.array(Image.open(dirname + tmp[0]).convert("L")).reshape(1, 400)
        data = numpy.row_stack((data, img))
        label = numpy.row_stack((label, int(tmp[1])))

    sio.savemat(matname, {'data': data, 'label': label})


function("./test/", "./test/test.txt", "./test/dataTrain.mat")
function("./train/", "./train/train.txt", "./train/dataTrain.mat")
