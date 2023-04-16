import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import window


class displayer:
    def __init__(self) -> None:
        self.dic = {
            "开心":"1.gif",
            "难过":"2.gif",
            "生气":"3.gif",
            "害羞":"4.gif",
            "惊讶":"5.gif",
            "疑惑":"6.gif",
            "委屈":"7.gif",
            "无语":"8.gif",
            "平淡":"9.gif"
        }
        self.app = QApplication(sys.argv)
        self.widget = window.picture()

    def modify(self,str):
        # print(str)
        # print(self.dic[str])
        if(self.dic.get(str) == None):
            print("表情不存在")
            self.widget.changeimage(self.dic["平淡"])
            return
        self.widget.changeimage(self.dic[str])


# app = QApplication(sys.argv)

# test = displayer()

# print(test)

# # test.modify("难过")

# sys.exit(app.exec())    
       
