import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from multidim_gui.multidim_analysis import Ui_MainWindow
from utils.image_process import array_to_QImage
from li.draw_graph import Demo
from chen.draw_graph import draw_records


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

        self.li_project = Demo()
        self.pushButton_1.clicked.connect(lambda: self.set_label_pixmap(
            self.graphLabel, self.li_project.drawPie("OP30厚度检测气缸伸出未到位")))

        self.pushButton_2.clicked.connect(lambda: self.set_label_pixmap(
            self.graphLabel, self.li_project.drawBarAndLine("OP30厚度检测气缸伸出未到位")))

        self.pushButton_3.clicked.connect(lambda: self.set_label_pixmap(
            self.graphLabel, self.li_project.drawMultipleToday("OP30")))

        self.pushButton_4.clicked.connect(lambda: self.set_label_pixmap(
            self.graphLabel, self.li_project.drawMultipleWeek("OP30")))

        self.pushButton_5.clicked.connect(lambda: self.set_label_pixmap(
            self.graphLabel, draw_records("sawanini_1")))

        self.pushButton_6.clicked.connect(lambda: self.set_label_pixmap(
            self.graphLabel, draw_records("sawanini_2")))

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        pass  # size设为None表示图片大小自适应

    @pyqtSlot(bool)
    def process_exit(self, trigger):
        sys.exit()

    def set_label_pixmap(self, label, img):
        qimage = array_to_QImage(img, label.size())
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
