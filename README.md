#caffe训练识别USTC教务系统验证码

参考[博客](http://home.cahhbwy.cn/index.php/2017/02/23/blog/)

下载文件夹[参考方法](https://www.zhihu.com/question/25369412)

getImage.py用来下载图片

data.tgz是图片(tar.gz压缩)

makeData.py用来生成标签

create_lmdb.bat用来生成lmdb文件

test_lmdb和train_lmdb是lmdb格式的测试数据集和训练数据集

lenet_solver.prototxt是配置文件

lenet_train_test.prototxt是网络结构

train_lenet.bat是训练命令

misustc_iter.caffemodel是我得到的一个较好的model

misustc_iter.solverstate保存当时的训练状态

deploy.prototxt是测试用的网络，基于lenet_train_test.prototxt修改

getImage_Classify.py用来获取文件并分文件夹放好

test.py测试模型并输出网络的一些信息
