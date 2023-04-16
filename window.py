import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap,QMovie


class picture (QWidget):
    def __init__(self):
        super ().__init__()
        self.lbl = QLabel(self)
        self.initUI ()

    def initUI(self):
        
        self.gif = QMovie('1.gif')
        self.lbl.setMovie(self.gif)
        self.gif.start()
        # pixmap = QPixmap("/home/toybrick/Desktop/project/static/1.jpg")  # 按指定路径找到图片
        self.lbl.setFixedSize(800,600)
        self.lbl.setScaledContents (True)  # 让图片自适应label大小
        hbox = QHBoxLayout()   
        hbox.addWidget(self.lbl)

        self.setLayout(hbox)
        # self.move (300, 200)
        self.setWindowTitle ('chatDog')
        self.show ()

    def changeimage(self,str):
        # pixmap = QPixmap("./smile2.png")
        self.gif = QMovie(str)
        self.lbl.setMovie(self.gif)

'''
app = QApplication(sys.argv)
widget = picture()
# widget.changeimage()
# widget.resize(640, 480)
# widget.setWindowTitle("Hello, PyQt5!")
# widget.show()
sys.exit(app.exec())
'''