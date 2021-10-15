# Chinese-Porcelain-Art-Classification

## cultureRelicRecognition.ipynb

1. Type: python file
2. Open the tool: jupyter notebook
3. Realize function:
   1. Customize the data set and realize the way to get image and label
   2. Define the model: use the official pre-training model
   3. Training model: a total of three models are trained, namely: alexnet, vgg13, vgg16

## system

1. system.py: The python file that implements the system interface, using the PyQt5 framework
2. system.ui: The layout file of the system interface, you can use Qt Desginer to open, modify and design
3. ui.py: python file converted from system.ui via command line

## models

1. AlexNet.pth: A model trained on the basis of the AlexNet pre-trained model using the cultural relics data set
2. alexnet-owt-7be5be79.pth: the pre-trained model of AlexNet officially provided by Pytorch
3. VGG13.pth: a model trained on the basis of the VGG13 pre-training model using the cultural relics data set
4. vgg13_bn-abd245e5.pth: the pre-trained model of VGG13 officially provided by Pytorch
5. VGG16.pth: A model trained on the basis of the VGG16 pre-training model using the cultural relics data set
6. vgg16_bn-6c64b313.pth: the pre-trained model of VGG16 officially provided by Pytorch

## train

1. train.csv: record the correspondence between pictures and their categories
2. imgs: training data set
   1. Category: 6
   2. The amount of data in each category: (jin, 270), (tang, 238), (song, 217)
      (Yuan, 279), (ming, 270), (qing, 274)

## val

1. val.csv: Record the corresponding relationship between pictures and data in the verification set
2. imgs: validation data set
   1. Category: 6
   2. The amount of data in each category: (jin, 30), (tang, 30), (song, 30)
      (Yuan, 30), (ming, 30), (qing, 30)

## test

1. imgs: test data

## Data style description

1. jin: pot (earth color, partial pottery) tang: bottle (partial pottery, earthy color)
2. song: bowl (pure color, porcelain style) yuan: bottle (long neck)
3. ming: bowl (blue and white porcelain style) qing: plate (colorful)
