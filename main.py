import smtplib
import sys
import os

import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidget, QMessageBox, QDialog, QRadioButton

from config import email_address
from multidim_gui.multidim_analysis_v2 import Ui_MainWindow
from multidim_gui.send_email_report_dialog import Ui_sendEmailDialog
from utils.image_process import array_to_QImage, fig2img
from li.draw_graph import Demo
from li.fetchMessage import Message
from chen.draw_graph import draw_records
from chen.email_report import get_records_report
from utils.send_email import Email
from wang.get_analysis_report import get_analysis_report
from wang.draw import Draw
from wang.figure_plot import Figure_OEE
from yv.analysis_report import report_summarize
from yv.opc_plot import FigureLineChart


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stop.triggered.connect(self.process_exit)
        self.fullScreen.triggered.connect(self.showFullScreen)
        self.exitFullScreen.triggered.connect(self.showNormal)
        self.setupMenu.triggered.connect(lambda: os.system("notepad config.py"))
        self.openEmailReport.triggered.connect(self.open_send_email_dialog)
        self.treeWidget.expandAll()

        self.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
            lambda item, col: self.set_label_pixmap(self.get_project_chart(item.text(col))))

        self.li_project = Demo()
        self.yv_project = FigureLineChart()
        self.wang_project = Draw()

        self.send_email_report_dialog = None

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

    @pyqtSlot(bool)
    def open_send_email_dialog(self, triggered):
        self.send_email_report_dialog = SendEmailDialog(self)
        self.send_email_report_dialog.show()
        # self.send_email_report_dialog.exec()


class SendEmailDialog(QDialog, Ui_sendEmailDialog):
    def __init__(self, statistic_window):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("发送邮件报告")
        self.statistic_window = statistic_window

        self.lineEdit.setText(email_address)
        self.buttonBox.accepted.connect(self.button_box_accepted)
        self.radioButton_1.toggled.connect(lambda checked: self.toggle_radio_button(
            "wang", checked))
        self.radioButton_2.toggled.connect(lambda checked: self.toggle_radio_button(
            "chen", checked))
        self.radioButton_3.toggled.connect(lambda checked: self.toggle_radio_button(
            "yv", checked))
        self.radioButton_4.toggled.connect(lambda checked: self.toggle_radio_button(
            "li", checked))

        self.email_content = {
            'wang': '',
            'chen': '',
            'yv': '',
            'li': '',
        }

    def toggle_radio_button(self, project_name: str, is_down: bool):
        print(project_name, is_down)
        if not is_down:
            self.email_content[project_name] = ""
            self.textEdit.clear()
            for cont in self.email_content.values():
                self.textEdit.append(cont)
        else:
            self.email_content[project_name] = self.get_email_content(project_name)
            self.textEdit.append(self.email_content[project_name])

    @pyqtSlot()
    def button_box_accepted(self):
        success = self.send_email_records("生产流程的多维分析与可视化-统计报告", self.textEdit.toPlainText(), self.lineEdit.text())
        msg_box = QMessageBox()
        msg_box.setWindowTitle("邮件发送反馈")
        if success:
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("报告邮件发送成功^_^ ")
        else:
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("报告邮件发送失败！!")
        msg_box.show()
        msg_box.exec()

    def get_email_content(self, project_name: str) -> str:
        if project_name == 'chen':
            return get_records_report()
        elif project_name == 'li':
            return Message.transmitReporter("OP20") + \
                   Message.transmitReporter("OP30") + \
                   Message.transmitReporter("OP40")
        elif project_name == "wang":
            return get_analysis_report()
        elif project_name == "yv":
            return report_summarize()
        return ""

    @staticmethod
    def send_email_records(subject: str, content: str, to_account: str) -> bool:
        try:
            Email.send_email(subject, content, from_account="layhal@163.com", SMTP_host="smtp.163.com",
                             from_password="liu670", to_account=to_account)
            print("邮件报告发送成功")
            return True
        except smtplib.SMTPException or Exception as e:
            print("邮件报告发送失败！", e)
            return False


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
