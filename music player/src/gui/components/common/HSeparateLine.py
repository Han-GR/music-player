from PyQt5.QtWidgets import QFrame


class HSeparateLine(QFrame):
    def __init__(self):
        super(HSeparateLine, self).__init__()

        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
