import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap,QMovie
import window


class displayer:
    def __init__(self) -> None:
        self.dic = {
            "开心":"2.gif",
            "难过":"7.gif",
            "生气":"11.gif",
            "害羞":"9.gif",
            "惊讶":"5.gif",
            "疑惑":"14.gif",
            "委屈":"7.gif",
            "无语":"8.gif",
            "平淡":"1.gif",
            "倾听":"12.gif"
        }
        self.gifs = {}
        self.app = QApplication(sys.argv)
        for k,v in self.dic.items():
            gif = QMovie(v)
            gif.start()
            self.gifs[k] = gif
        self.widget = window.picture()

    def modify(self,str,loop:bool=False):
        # print(str)
        # print(self.dic[str])
        print("[debug] the emotion key word is :" + str)
        # self.widget.changeimage(self.gifs["惊讶"])
        if(self.gifs.get(str) == None):
            print("[debug] the key word does not exsit")
            self.widget.changeimage(self.gifs["平淡"],loop)
            return
        self.widget.changeimage(self.gifs[str],loop)


# app = QApplication(sys.argv)

# test = displayer()

# print(test)

# # test.modify("难过")

# sys.exit(app.exec())    
       
