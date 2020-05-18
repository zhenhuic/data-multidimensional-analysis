import sys
import os

import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidget

from multidim_gui.multidim_analysis_v2 import Ui_MainWindow
from utils.image_process import array_to_QImage, fig2img
from li.draw_graph import Demo
from chen.draw_graph import draw_records
from wang.draw import Draw
from wang.figure_plot import Figure_OEE
from yv.opc_plot import FigureLineChart


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

        self.li_project = Demo()
        self.yv_project = FigureLineChart()
        self.wang_project = Draw()

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
        # chen
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

        # li
        elif item_name == "OP20今日报警频次":
            return self.li_project.drawMultipleToday("OP20")
        elif item_name == "OP20一周报警情况":
            return self.li_project.drawMultipleWeek("OP20")
        elif item_name == "OP20侧气压低":
            return self.li_project.drawPie("OP20侧气压低")
        elif item_name == "OP20冲床报警":
            return self.li_project.drawBarAndLine("OP20冲床报警")

        elif item_name == "OP30今日报警频次":
            return self.li_project.drawMultipleToday("OP30")
        elif item_name == "OP30一周报警情况":
            return self.li_project.drawMultipleWeek("OP30")
        elif item_name == "OP30机器人急停":
            return self.li_project.drawPie("OP30机器人急停")
        elif item_name == "OP30码垛产品不一致":
            return self.li_project.drawBarAndLine("OP30码垛产品不一致")

        elif item_name == "OP40今日报警频次":
            return self.li_project.drawMultipleToday("OP40")
        elif item_name == "OP40一周报警情况":
            return self.li_project.drawMultipleWeek("OP40")
        elif item_name == "OP40安全门未锁":
            return self.li_project.drawPie("OP40安全门未锁")
        elif item_name == "OP40宽度检测气缸缩回未到位":
            return self.li_project.drawBarAndLine("OP40宽度检测气缸缩回未到位")

        # yv
        # 侧板焊接线
        elif item_name == "焊接启动":
            self.yv_project.plotlinechart("hanjie", "日平均(7日)", "焊接启动", "计数")
            return cv2.imread("1.png")
        elif item_name == "送丝":
            self.yv_project.plotlinechart("hanjie", "日平均(7日)", "送丝", "计数")
            return cv2.imread("1.png")
        elif item_name == "油泵开":
            self.yv_project.plotlinechart("hanjie", "日平均(7日)", "油泵开", "计数")
            return cv2.imread("1.png")
        # 新萨瓦尼尼线
        elif item_name == "门板前左角度":
            self.yv_project.plotlinechart("xinsawanini", "日平均(7日)", "门板前左角度", "计数")
            return cv2.imread("1.png")
        elif item_name == "门板中部左角度":
            self.yv_project.plotlinechart("xinsawanini", "日平均(7日)", "门板中部左角度", "计数")
            return cv2.imread("1.png")
        elif item_name == "门板后左角度":
            self.yv_project.plotlinechart("xinsawanini", "日平均(7日)", "门板后左角度", "计数")
            return cv2.imread("1.png")
        elif item_name == "门板前右角度":
            self.yv_project.plotlinechart("xinsawanini", "日平均(7日)", "门板前右角度", "计数")
            return cv2.imread("1.png")
        elif item_name == "门板中部右角度":
            self.yv_project.plotlinechart("xinsawanini", "日平均(7日)", "门板中部右角度", "计数")
            return cv2.imread("1.png")
        elif item_name == "门板后右角度":
            self.yv_project.plotlinechart("xinsawanini", "日平均(7日)", "门板后右角度", "计数")
            return cv2.imread("1.png")

        # wang
        elif item_name == "侧板设备工作损失占比":
            return self.wang_project.draw_fp()
        elif item_name == "侧板OEE能效日推图":
            return self.wang_project.draw_oee()
        elif item_name == "侧板设备工作损失时间统计":
            return self.wang_project.draw_loss()

        # yue

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
