clear
clc
[savestr, status] = urlwrite(['http://mis.teach.ustc.edu.cn/randomImage.do?data=''' int2str(randi(9846513215)) ''''], 'tmp.jpg', 'timeout', 15);
if(status ~= 1)
    fprintf('download Image Error!\n')
    return
end

img = rgb2gray(imread('tmp.jpg'));
img(img>140)=255;
img=im2single(img);
im1=permute(img(:,1:20), [2, 1, 3]);
im2=permute(img(:,21:40), [2, 1, 3]);
im3=permute(img(:,41:60), [2, 1, 3]);
im4=permute(img(:,61:80), [2, 1, 3]);
figure;
imshow(img);

labels = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ';
model = 'deploy.prototxt';
weights = 'misustc_iter.caffemodel';

caffe.set_mode_cpu();
net = caffe.Net(model,weights,'test');
net.blobs('data').reshape([20 20 1 4]);
net.reshape()
net.blobs('data').set_data(reshape([im1,im2,im3,im4],net.blobs('data').shape));
net.forward_prefilled();
result=net.blobs('prob').get_data();
[maxpro,index]=max(result);
fprintf('predicted class is: %d\n',index);
fprintf('output label: %c\n',labels(index));

needShow=true;
if(needShow)
    shape=net.params('conv1',1).shape;
    tmp=net.params('conv1',1).get_data();
    size=ceil(sqrt(shape(4)));
    figure;
    for i=1:shape(4)
        subplot(size,size,i);
        imshow(tmp(:,:,1,i),[]);
    end
    suptitle('卷积核');

    shape=net.blobs('conv1').shape;
    tmp=net.blobs('conv1').get_data();
    figure;
    for k=1:4
        for i=1:shape(3)
            subplot(4,shape(3),(k-1)*shape(3)+i);
            imshow(tmp(:,:,i,k)',[]);
        end
    end
    suptitle('conv1输出');

    tmp=net.blobs('ip2').get_data();
    figure;
    subplot(2, 1, 1);
    plot(tmp);
    title('ip2输出');
    tmp=net.blobs('prob').get_data();
    subplot(2, 1, 2);
    plot(tmp);
    title('概率值');
end

caffe.reset_all();