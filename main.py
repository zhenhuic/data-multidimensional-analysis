import subprocess
import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from gui.multidim_analysis import Ui_MainWindow
from utils.pixmap_prep import images_prep_factory, array_to_QImage


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stop.triggered.connect(self.process_exit)
        self.fullScreen.triggered.connect(self.showFullScreen)
        self.exitFullScreen.triggered.connect(self.showNormal)
        self.setupMenu.triggered.connect(lambda: os.system("notepad config.py"))

        self.chen1.triggered.connect(self.set_label_pixmap)
        self.chen2.triggered.connect(self.set_label_pixmap)
        self.li.triggered.connect(self.set_label_pixmap)
        self.yv1.triggered.connect(self.set_label_pixmap)
        self.yv2.triggered.connect(self.set_label_pixmap)
        self.wang.triggered.connect(self.set_label_pixmap)
        self.pan.triggered.connect(self.set_label_pixmap)
        self.yue.triggered.connect(self.set_label_pixmap)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        pass  # size设为None表示图片大小自适应

    @pyqtSlot(bool)
    def process_exit(self, trigger):
        sys.exit()

    def set_label_pixmap(self, label, name, size):
        if self.label_images_dict[name] is not None:
            if size is None:
                size = label.size()
            qimage = array_to_QImage(self.label_images_dict[name][0], size)
            label.setPixmap(QPixmap.fromImage(qimage))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
