import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap,QMovie


class picture (QWidget):
    def __init__(self):
        super ().__init__()
        self.lbl = QLabel(self)
        self.initUI ()

    def initUI(self):
        
        self.defalutgif = QMovie('1.gif')
        self.defalutgif.start()
        self.lbl.setMovie(self.defalutgif)
        # pixmap = QPixmap("/home/toybrick/Desktop/project/static/1.jpg")  # 按指定路径找到图片
        self.lbl.setFixedSize(1280,720)
        self.lbl.setScaledContents (True)  # 让图片自适应label大小
        hbox = QHBoxLayout()   
        hbox.addWidget(self.lbl)

        self.setLayout(hbox)
        # self.move (300, 200)
        self.setWindowTitle ('chatDog')
        self.show ()

    def changeimage(self,newMovie:QMovie,loop:bool=False,idle:QMovie=None):
        # pixmap = QPixmap("./smile2.png")
        # print("[debug] in changeImage() : the src is "+newMovie)
        # self.gif = QMovie(str)
        if idle==None:
            idle = self.defalutgif
        cnt = 1
        if not loop:
            while cnt!=0:
                cnt = newMovie.currentFrameNumber()
        self.lbl.setMovie(newMovie)
        print("[debug] in changeImage() : the Movie is reset")
        if not loop:
            cnt = newMovie.currentFrameNumber()
            while cnt==0:
                cnt = newMovie.currentFrameNumber()
            while cnt!=0:
                cnt = newMovie.currentFrameNumber()
            self.lbl.setMovie(idle)
        # self.gif.start()

'''
app = QApplication(sys.argv)
widget = picture()
# widget.changeimage()
# widget.resize(640, 480)
# widget.setWindowTitle("Hello, PyQt5!")
# widget.show()
sys.exit(app.exec())
'''
