import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class picture (QWidget):
    def __init__(self):
        super ().__init__()
        self.lbl = QLabel(self)
        self.initUI ()

    def initUI(self):
        
        pixmap = QPixmap("/home/toybrick/Desktop/project/static/1.jpg")  # 按指定路径找到图片
        self.lbl.setFixedSize(800,600)
        self.lbl.setPixmap (pixmap)  # 在label上显示图片
        self.lbl.setScaledContents (True)  # 让图片自适应label大小
        hbox = QHBoxLayout()   
        hbox.addWidget(self.lbl)

        self.setLayout(hbox)
        # self.move (300, 200)
        self.setWindowTitle ('pic')
        self.show ()

    def changeimage(self,str):
        # pixmap = QPixmap("./smile2.png")
        pixmap = QPixmap(str)
        self.lbl.setPixmap(pixmap)
        self.resize(600,800)

'''
app = QApplication(sys.argv)
widget = picture()
# widget.changeimage()
# widget.resize(640, 480)
# widget.setWindowTitle("Hello, PyQt5!")
# widget.show()
sys.exit(app.exec())
'''