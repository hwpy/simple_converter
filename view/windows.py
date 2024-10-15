
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QListWidget,
    QMessageBox,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from model.main_window import FileListSettings


class MainWindowElements:
    def __init__(self) -> None:

        self.file_list = QListWidget()
        self.file_list.setGeometry(
            FileListSettings.xpadd.value,
            FileListSettings.ypadd.value,
            FileListSettings.width.value,
            FileListSettings.height.value
        )

        self.msg_converted = QMessageBox()

        self.button_convert = QPushButton("Конвертировать")
        self.button_open = QPushButton("Открыть файл")

        self.slider_quality = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_subsampling = QSlider(Qt.Orientation.Horizontal, self)

        self.layout = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
