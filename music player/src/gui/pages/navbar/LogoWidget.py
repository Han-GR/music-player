from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.utils.ImgConverter import ToCircleImg


class LogoWidget(QWidget):
    mouseDoubleClick = pyqtSignal()

    def __init__(self):
        super(LogoWidget, self).__init__()

        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.initUI()

    def initUI(self):
        logoUrl = '../../resource/img/logo.png'
        logoSize = 50

        layout = QHBoxLayout()
        self.setLayout(layout)

        logo = QLabel()
        logo.setPixmap(ToCircleImg(logoUrl, logoSize, logoSize, self))
        layout.addWidget(logo)

        title = QLabel("哈喽")
        title.setStyleSheet("font-size:30px;color:#FFFFFF;font-weight:bold;")
        layout.addWidget(title)

        layout.addStretch(1)

    # 重写鼠标双击事件
    def mouseDoubleClickEvent(self, event):
        self.mouseDoubleClick.emit()
