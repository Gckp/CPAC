# Chinese-Porcelain-Art-Classification

---cultureRelicRecognition.ipynb---
类型：python文件
打开工具：jupyter notebook
实现功能：
1.自定义了数据集，实现了取image和label的方式
2.定义模型：使用了官方提供的预训练模型
2.训练模型：总共训练了三个模型，分别是：alexnet、vgg13、vgg16

---system---
        |----system.py：实现系统界面的python文件，使用了PyQt5框架
        |----system.ui：系统界面的布局文件，可以使用Qt Desginer打开修改和设计
        |----ui.py：       system.ui通过命令行转换得到的python文件

---models---
        |----AlexNet.pth：使用文物数据集在AlexNet预训练模型的基础上训练得到的模型
        |----alexnet-owt-7be5be79.pth：Pytorch官方提供的AlexNet的预训练模型
        |----VGG13.pth：使用文物数据集在VGG13预训练模型的基础上训练得到的模型
        |----vgg13_bn-abd245e5.pth：Pytorch官方提供的VGG13的预训练模型
        |----VGG16.pth：使用文物数据集在VGG16预训练模型的基础上训练得到的模型
        |----vgg16_bn-6c64b313.pth：Pytorch官方提供的VGG16的预训练模型

---train---
        |----train.csv：记录图片与其类别的对应关系
        |----imgs：训练数据集
                         类别：6
                         各个类别的数据量：（jin，270）、    （tang，238）、（song，217）
	                                      （yuan，279）、（ming，270）、（qing，274）

----val----
        |----val.csv：记录验证集中图片与数据的对应关系
        |----imgs：验证数据集
                         类别：6
                         各个类别的数据量：（jin，30）、    （tang，30）、 （song，30）
	                                      （yuan，30）、（ming，30）、（qing，30）
---test---
       |----imgs：测试数据

---数据风格说明---
jin：罐（土色，偏陶器）                   tang：瓶（偏陶器，土色）     
song：碗（纯色，瓷器风格）            yuan：瓶（长颈）     
ming：碗（青花瓷风格）                  qing：盘（多彩）