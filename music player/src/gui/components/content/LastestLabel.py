from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 音乐标题栏按钮
from gui.utils.TimeFormatter import timeStamptoTime


class LastestLabel(QLabel):

    def __init__(self, lastestTime):
        super(LastestLabel, self).__init__()

        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setText(self.getText(lastestTime))

    def getText(self, lastestTime):
        return timeStamptoTime(lastestTime)
