import os
import sys
from PIL import Image, ImageQt
from PyQt5.QtWidgets import *
from ui import Ui_MainWindow

import torch
import  torchvision.models as models
import torchvision.transforms as tf

class myWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.initUI()
        self.initArgv()
        self.initSlot()

    def initUI(self):
        '''
        function: initialize the layout of the window
        '''
        self.win = QMainWindow()
        self.setupUi(self.win)

    def initArgv(self):
        '''
        function  : initialize kinds of parameters
        parameters: device   : cuda or cpu
                    models   : three model we use in this project
                    net      : one of the models we use to classify the image
                    transform: a series of operations on input images

        '''
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.models = {
            'AlexNet':models.alexnet(pretrained=False),
            'VGG13':models.vgg13_bn(pretrained=False),
            'VGG16':models.vgg16_bn(pretrained=False)
        }
        self.net = None
        self.dynastics = {0:'Jin', 1:'Tang', 2:'Song', 3:'Yuan', 4:'Ming', 5:'Qing'}
        self.transform = tf.Compose([
            tf.Resize(256),
            tf.CenterCrop(224),
            tf.ToTensor(),
            tf.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
        ])


    def initSlot(self):
        '''
        function  : connect the slots and signals
        @1: trigger selectModel function when modelBtn is clicked
        @2: trigger selectImage function when imageBtn is clicked
        @3: trigger clearResults function when imageBtn is clicked
        @4: trigger recognizeImage function when recognitionBtn is clicked
        '''
        self.modelBtn.clicked.connect(self.selectModel)
        self.imageBtn.clicked.connect(self.selectImage)
        self.imageBtn.clicked.connect(self.clearResults)
        self.recognitionBtn.clicked.connect(self.recognizeImage)

    def selectModel(self):
        '''
        function: select a model to classify input image
        '''
        fileName, fileType = QFileDialog.getOpenFileName(
            self,
            'select model',
            os.path.abspath(os.path.dirname(os.getcwd())),
            "Pth Files(*.pth)")
        
        if  fileName== "":
            msg = QMessageBox.warning(self, 'Warning', 'Please select a model', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.modelPath.setText(fileName)
            self.loadModel(fileName)

    def loadModel(self, path):
        '''
        function  : load the trained model to self.net after the model was selected
        parameters: path: path of selected trained model 
        '''
        print(path)
        model_name = path[len(os.getcwd()+'/') : len(path)].split('.')
        model_name = model_name[0]
        self.net = self.models[model_name]
        self.net.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
        msg = QMessageBox.information(None, 'Hint', 'Load Finished', QMessageBox.Yes)
        

    def selectImage(self):
        '''
        function: select an image from files
        '''
        fileName, fileType = QFileDialog.getOpenFileName(
            self,
            'select image',
            os.path.abspath(os.path.dirname(os.getcwd())),
            "Jpg Files(*.jpg);;Png Files(*.png)")
        if fileName == "":
            msg = QMessageBox.warning(self, 'Warning', 'Please select an image', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.imagePath.setText(fileName)
            self.showImage(fileName)

    def showImage(self, path):
        '''
        function  : display selected image in self.imageArea
        parameters: path: path of selected image
        '''
        img = Image.open(path)
        w, h = img.size
        if w > 481 and h < 281:
            r = w / 481
            img = img.resize((481, int(h/r)), 4)
        elif h > 281 and w < 481:
            r = h / 281
            img = img.resize((int(w/r), 281), 4)
        elif h > 281 and w > 481:
            r = h/281
            img = img.resize((int(w/r), 281), 4)
        img = ImageQt.toqpixmap(img)
        self.imageArea.setPixmap(img)

    def recognizeImage(self):
        '''
        function: classify the input image using self.net
        '''
        if self.modelPath.text()=="":
            msg = QMessageBox.warning(self, 'Warning', 'Please select a model', QMessageBox.Ok, QMessageBox.Ok)
        elif self.imagePath.text()=="":
            msg = QMessageBox.warning(self, 'Warning', 'Please select an image', QMessageBox.Ok, QMessageBox.Ok)
        else:
            img = Image.open(self.imagePath.text()).convert('RGB')
            img = self.transform(img)
            # img.shape ---> [3, 224, 224]
            img = img.unsqueeze(dim=0)
            # img.shape ---> [1, 3, 224, 224]
            # [batch_size, channels, width, height]
            self.net.eval()
            with torch.no_grad(): 
                out = self.net(img)
                # out.shape ---> [1, 6]
                self.setResults(out)
        
    def clearResults(self):
        '''
        function: clear the outputs below the imageArea
        '''
        self.resultLabel.setText('')
        self.jinBar.setValue(0)
        self.tangBar.setValue(0)   
        self.songBar.setValue(0)
        self.yuanBar.setValue(0)
        self.mingBar.setValue(0)
        self.qingBar.setValue(0) 
            
    def setResults(self, out):
        '''
        function: set the value of every progress bar below imageArea
        '''
        index = torch.max(out, dim=1)[1].item()
        self.resultLabel.setText(self.dynastics[index])
        prob = torch.softmax(out, dim=1)[0]
        prob = (prob*100).numpy()
        self.jinBar.setValue(prob[0])
        self.tangBar.setValue(prob[1])   
        self.songBar.setValue(prob[2])
        self.yuanBar.setValue(prob[3])
        self.mingBar.setValue(prob[4])
        self.qingBar.setValue(prob[5])  

    def show(self):
        '''
        function: display the window
        '''
        self.win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())