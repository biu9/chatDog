import display
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)
test = display.displayer()
sys.exit(app.exec())   
test.modify('开心')