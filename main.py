import sys
from PyQt5.QtWidgets import QApplication
from main_gui import WgimgscraperApp

if __name__ == '__main__':
    gui_app = QApplication(sys.argv)
    app = WgimgscraperApp()
    app.show()

    sys.exit(gui_app.exec_())
