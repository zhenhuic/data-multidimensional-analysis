import sys
import os

import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidget

from multidim_gui.multidim_analysis_v2 import Ui_MainWindow
from utils.image_process import array_to_QImage
from li.draw_graph import Demo
from chen.draw_graph import draw_records
from wang.figure_plot import Figure_OEE


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stop.triggered.connect(self.process_exit)
        self.fullScreen.triggered.connect(self.showFullScreen)
        self.exitFullScreen.triggered.connect(self.showNormal)
        self.setupMenu.triggered.connect(lambda: os.system("notepad config.py"))
        self.treeWidget.expandAll()

        self.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
            lambda item, col: self.set_label_pixmap(self.get_project_chart(item.text(col))))


        # self.li_project = Demo()
        # self.pushButton_1.clicked.connect(lambda: self.set_label_pixmap(
        #     self.graphLabel, self.li_project.drawPie("OP30厚度检测气缸伸出未到位")))
        #
        # self.pushButton_2.clicked.connect(lambda: self.set_label_pixmap(
        #     self.graphLabel, self.li_project.drawBarAndLine("OP40定位台宽度检测气缸缩回到位")))
        #
        # self.pushButton_3.clicked.connect(lambda: self.set_label_pixmap(
        #     self.graphLabel, self.li_project.drawMultipleToday("OP30")))
        #
        # self.pushButton_4.clicked.connect(lambda: self.set_label_pixmap(
        #     self.graphLabel, self.li_project.drawMultipleWeek("OP30")))
        #
        # self.pushButton_5.clicked.connect(lambda: self.set_label_pixmap(
        #     self.graphLabel, draw_records("sawanini_1")))
        #
        # self.pushButton_6.clicked.connect(lambda: self.set_label_pixmap(
        #     self.graphLabel, draw_records("baobantongyong")))
        # oee = Figure_OEE()
        # self.pushButton_7.clicked.connect(lambda: self.set_label_pixmap(
        #     self.graphLabel, oee.plot(*(33, 28, 37, 94))))

    def get_project_chart(self, item_name: str) -> np.ndarray:
        print('"' + item_name + '"')
        if item_name == "老萨瓦尼尼线":
            return draw_records("sawanini_1")
        elif item_name == "新萨瓦尼尼线":
            return draw_records("sawanini_2")
        elif item_name == "专机下线":
            return draw_records("zhuanjixia")
        elif item_name == "喷粉上线":
            return draw_records("penfenshang")
        elif item_name == "薄板通用线":
            return draw_records("baobantongyong")


        else:
            print("未设置该项目")
            return None

    def set_label_pixmap(self, img):
        if img is not None:
            qimage = array_to_QImage(img, self.graphLabel.size())
            self.graphLabel.setPixmap(QPixmap.fromImage(qimage))

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        pass  # size设为None表示图片大小自适应

    @pyqtSlot(bool)
    def process_exit(self, trigger):
        sys.exit()


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
