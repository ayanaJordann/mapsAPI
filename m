import sys
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
import requests

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        uic.loadUi('main_window.ui',self)
        self.zoom = 10
        self.ll = []
        self.api_key = ''

    def show_map(self):
        map_params = {}
        api_server = ''
        response = requests.get(api_server, params=map_params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(response.url)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        map_image = QImage.fromData(response.content)
        pixmap = QPixmap.fromImage(map_image)
        self.g_map.setPixmap(pixmap)



if __name__='__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
