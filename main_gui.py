from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, \
    QVBoxLayout, QFileDialog, QMessageBox
from scraper import imgscraper


class WgimgscraperApp(QWidget):
    def __init__(self):
        super().__init__()

        self.file_select = None

        # initial
        self.resize(500, 150)
        self.setFixedSize(self.size())

        # widgets

        self.select_dir_button = QPushButton('Select Directory')

        self.start_download_button = QPushButton('Start Download')
        self.thread_id_line_edit = QLineEdit()
        self.thread_id_line_edit.setPlaceholderText("ThreadID example: 7704852")
        self.info_label = QLabel('Enter a thread ID in order to extract all '
                                 'images')
        self.currently_selected_dir = QLabel('Currently Selected Directory: '
                                             'None')

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.thread_id_line_edit)
        layout.addWidget(self.currently_selected_dir)
        layout.addWidget(self.select_dir_button)
        layout.addWidget(self.start_download_button)

        self.setLayout(layout)

        # on click events
        self.select_dir_button.clicked.connect(self.get_dir)
        self.start_download_button.clicked.connect(self.start_download)

    @pyqtSlot()
    def get_dir(self):
        self.file_select = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.currently_selected_dir.setText(f'Currently Selected Directory: '
                                            f'\n{self.file_select}')

    @pyqtSlot()
    def start_download(self):
        if self.file_select is None:
            msg = QMessageBox()
            msg.setWindowTitle("Missing Download Directory!")
            msg.setText("Missing Download Directory!")
            msg.exec_()
        elif len(self.thread_id_line_edit.text()) != 7:
            msg = QMessageBox()
            msg.setWindowTitle("Malformed Thread-ID")
            msg.setText("Malformed Thread-ID")
            msg.exec_()
        else:
            thread_id = self.thread_id_line_edit.text()
            directory = self.file_select
            exit_code_of_imgscraper: int = imgscraper(thread_id=thread_id,
                                                      dir_to_store=directory)
            # TODO: add progress bar functionality here!!!
