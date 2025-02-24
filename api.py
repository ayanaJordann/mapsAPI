import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap, QImage, QTransform
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QButtonGroup
import requests
SCREEN_SIZE = [800, 800]


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.zoom = 7
        self.api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
        self.server_address = 'http://static-maps.yandex.ru/v1'
        self.ll = (44.269759,46.307743)
        self.map_request = f'{self.server_address}?apikey={self.api_key}&ll={f'{self.ll[0]},{self.ll[1]}'}&z={self.zoom}'
        request = requests.get(self.map_request)
        img = QImage.fromData(request.content)

        self.pixmap = QPixmap.fromImage(img)
        self.image = QLabel(self)
        self.image.move(120, 20)
        self.image.resize(600, 600)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
