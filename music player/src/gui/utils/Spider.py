import requests
from PyQt5.QtGui import *


def getPixmapByUrl(url):
    data = requests.get(url).content
    return QPixmap.fromImage(QImage.fromData(data))
