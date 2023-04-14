import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import window


class displayer:
    def __init__(self) -> None:
        self.dic = {
            "开心":"/home/toybrick/Desktop/project/static/1.jpg",
            "难过":"/home/toybrick/Desktop/project/static/2.jpg",
            "生气":"/home/toybrick/Desktop/project/static/3.jpg",
            "害羞":"/home/toybrick/Desktop/project/static/4.jpg",
            "惊讶":"/home/toybrick/Desktop/project/static/5.jpg",
            "疑惑":"/home/toybrick/Desktop/project/static/6.jpg",
            "委屈":"/home/toybrick/Desktop/project/static/7.jpg",
            "无语":"/home/toybrick/Desktop/project/static/8.jpg",
            "平淡":"/home/toybrick/Desktop/project/static/9.jpg"
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
       
