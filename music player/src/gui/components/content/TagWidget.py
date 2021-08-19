from PyQt5.QtWidgets import QWidget


class TagWidget(QWidget):

    def __init__(self, tag):
        super(TagWidget, self).__init__()
        self.tag = tag

    def getTag(self):
        return self.tag
