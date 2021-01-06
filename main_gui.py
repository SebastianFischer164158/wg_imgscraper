from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, \
    QVBoxLayout, QFileDialog

from scraper import imgscraper


class WgimgscraperApp(QWidget):
    def __init__(self):
        super().__init__()

        # initial
        self.resize(300, 150)
        self.setFixedSize(self.size())

        # widgets

        self.select_dir_button = QPushButton('Select Directory')

        self.start_download_button = QPushButton('Start Download')
        self.thread_id_line_edit = QLineEdit()
        self.thread_id_line_edit.setPlaceholderText("ThreadID example: 7704852")
        self.info_label = QLabel('Enter a thread ID in order to extract all '
                                 'images')

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.thread_id_line_edit)
        layout.addWidget(self.start_download_button)
        layout.addWidget(self.select_dir_button)

        self.setLayout(layout)

        # on click events
        self.select_dir_button.clicked.connect(self.get_dir)

    @pyqtSlot()
    def get_dir(self):
        file_select = QFileDialog.getExistingDirectory(self, 'Select Directory')

    @pyqtSlot()
    def start_download(self):
        pass
