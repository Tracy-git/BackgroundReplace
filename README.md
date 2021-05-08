# 证件照换底

## 目录
- <span id="jump"></span>[环境](#jump)
- <span id="jump"></span>[下载](#jump)
  -   <span id="jump"></span>[权重下载](#jump)
  -   <span id="jump"></span>[项目地址](#jump)
-  <span id="jump"></span>[用法](#jump) 


## 环境
1. python == 3.6
1. PyMatting==1.1.2
2. torchvision==0.8.0
3. torch==1.7.0+cu101
4. numpy==1.17.0
5. opencv_python==4.5.1.48
6. model1==1.0.4.8
7. Pillow==8.2.0

## 下载
- [权重下载](https://pan.baidu.com/s/1Q7MQMpQLcyQjkVvXxHANxQ) 提取码：trac
- [项目地址](https://pan.baidu.com/s/1esHpKM1um4Gi-8ry2L2aJw) 提取码：trac 

## 用法

1. 下载权重（链接见下载）
2. 下载项目文件，将权重放入model文件夹中
3. 在命令提示符页，输入python matting.py ，跳出选择图片框，选择要换底的证件照，然后确定，等待几秒，选择底色，直到提示转换完成。
