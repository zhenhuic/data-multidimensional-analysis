# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Lab417\data-multidimensional-analysis\multidim_gui\send_email_report_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sendEmailDialog(object):
    def setupUi(self, sendEmailDialog):
        sendEmailDialog.setObjectName("sendEmailDialog")
        sendEmailDialog.resize(720, 500)
        sendEmailDialog.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(85, 255, 255);")
        self.buttonBox = QtWidgets.QDialogButtonBox(sendEmailDialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 455, 620, 32))
        self.buttonBox.setStyleSheet("color: rgb(198, 198, 198);\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(66, 66, 66);\n"
"selection-background-color: rgb(45, 45, 45);\n"
"color: rgb(85, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(sendEmailDialog)
        self.textEdit.setGeometry(QtCore.QRect(90, 10, 620, 380))
        self.textEdit.setStyleSheet("gridline-color: rgb(25, 25, 25);\n"
"font: 12pt \"宋体\";\n"
"background-color: rgb(25, 25, 25);\n"
"border-color: rgb(25, 25, 25);\n"
"color: rgb(200, 200, 200);")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(sendEmailDialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 405, 620, 30))
        self.lineEdit.setStyleSheet("gridline-color: rgb(25, 25, 25);\n"
"font: 16pt \"宋体\";\n"
"background-color: rgb(25, 25, 25);\n"
"border-color: rgb(25, 25, 25);\n"
"color: rgb(200, 200, 200);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_1 = QtWidgets.QLabel(sendEmailDialog)
        self.label_1.setGeometry(QtCore.QRect(10, 5, 70, 35))
        self.label_1.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(85, 255, 255);")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(sendEmailDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 400, 70, 35))
        self.label_2.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(85, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.radioButton_1 = QtWidgets.QRadioButton(sendEmailDialog)
        self.radioButton_1.setGeometry(QtCore.QRect(5, 50, 80, 30))
        self.radioButton_1.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"font: 9pt \"微软雅黑\";\n"
"color: rgb(220, 220, 220);")
        self.radioButton_1.setAutoRepeat(True)
        self.radioButton_1.setAutoExclusive(False)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(sendEmailDialog)
        self.radioButton_2.setGeometry(QtCore.QRect(5, 90, 80, 30))
        self.radioButton_2.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"font: 9pt \"微软雅黑\";\n"
"color: rgb(220, 220, 220);")
        self.radioButton_2.setAutoRepeat(True)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(sendEmailDialog)
        self.radioButton_3.setGeometry(QtCore.QRect(5, 130, 80, 30))
        self.radioButton_3.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"font: 9pt \"微软雅黑\";\n"
"color: rgb(220, 220, 220);")
        self.radioButton_3.setAutoRepeat(True)
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(sendEmailDialog)
        self.radioButton_4.setGeometry(QtCore.QRect(5, 170, 80, 30))
        self.radioButton_4.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"font: 9pt \"微软雅黑\";\n"
"color: rgb(220, 220, 220);")
        self.radioButton_4.setAutoRepeat(True)
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName("radioButton_4")

        self.retranslateUi(sendEmailDialog)
        self.buttonBox.accepted.connect(sendEmailDialog.accept)
        self.buttonBox.rejected.connect(sendEmailDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(sendEmailDialog)

    def retranslateUi(self, sendEmailDialog):
        _translate = QtCore.QCoreApplication.translate
        sendEmailDialog.setWindowTitle(_translate("sendEmailDialog", "Dialog"))
        self.textEdit.setHtml(_translate("sendEmailDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_1.setText(_translate("sendEmailDialog", "邮件内容："))
        self.label_2.setText(_translate("sendEmailDialog", "邮箱地址："))
        self.radioButton_1.setText(_translate("sendEmailDialog", "设备效率"))
        self.radioButton_2.setText(_translate("sendEmailDialog", "异常监测"))
        self.radioButton_3.setText(_translate("sendEmailDialog", "多生产线"))
        self.radioButton_4.setText(_translate("sendEmailDialog", "PLC 节点"))
