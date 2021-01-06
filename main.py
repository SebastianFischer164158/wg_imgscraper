import sys
from PyQt5.QtWidgets import QApplication
from scraper import imgscraper
from main_gui import WgimgscraperApp


if __name__ == '__main__':
    # thread_id = "7690437"  # test case
    # exit_code_of_imgscraper: int = imgscraper(thread_id=thread_id)
    gui_app = QApplication(sys.argv)
    app = WgimgscraperApp()
    app.show()

    sys.exit(gui_app.exec_())