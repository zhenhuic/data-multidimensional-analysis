# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Lab417\data-multidimensional-analysis\multidim_gui\multidim_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.titleLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        self.titleLabel.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"font: 29pt \"宋体\";\n"
"color: rgb(90, 174, 242);\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(85, 255, 255);")
        self.titleLabel.setScaledContents(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setWordWrap(False)
        self.titleLabel.setIndent(0)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1280, 695))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 8, -1)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_1.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_2.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_2.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_3.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_4.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_5.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_6.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_7.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_8.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"font: 14pt \"宋体\";\n"
"color: rgb(85, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.graphLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.graphLabel.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.graphLabel.setText("")
        self.graphLabel.setObjectName("graphLabel")
        self.horizontalLayout_2.addWidget(self.graphLabel)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menuBar.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"selection-background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);")
        self.menuBar.setObjectName("menuBar")
        self.processMenu = QtWidgets.QMenu(self.menuBar)
        self.processMenu.setObjectName("processMenu")
        self.systemMenu = QtWidgets.QMenu(self.menuBar)
        self.systemMenu.setObjectName("systemMenu")
        self.setupMenu = QtWidgets.QMenu(self.menuBar)
        self.setupMenu.setObjectName("setupMenu")
        self.viewMenu = QtWidgets.QMenu(self.menuBar)
        self.viewMenu.setObjectName("viewMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.openConfigFile = QtWidgets.QAction(MainWindow)
        self.openConfigFile.setObjectName("openConfigFile")
        self.start = QtWidgets.QAction(MainWindow)
        self.start.setObjectName("start")
        self.stop = QtWidgets.QAction(MainWindow)
        self.stop.setObjectName("stop")
        self.chen1 = QtWidgets.QAction(MainWindow)
        self.chen1.setObjectName("chen1")
        self.chen2 = QtWidgets.QAction(MainWindow)
        self.chen2.setObjectName("chen2")
        self.li = QtWidgets.QAction(MainWindow)
        self.li.setObjectName("li")
        self.yv1 = QtWidgets.QAction(MainWindow)
        self.yv1.setObjectName("yv1")
        self.yv2 = QtWidgets.QAction(MainWindow)
        self.yv2.setObjectName("yv2")
        self.wang = QtWidgets.QAction(MainWindow)
        self.wang.setObjectName("wang")
        self.pan = QtWidgets.QAction(MainWindow)
        self.pan.setObjectName("pan")
        self.yue = QtWidgets.QAction(MainWindow)
        self.yue.setObjectName("yue")
        self.fullScreen = QtWidgets.QAction(MainWindow)
        self.fullScreen.setObjectName("fullScreen")
        self.exitFullScreen = QtWidgets.QAction(MainWindow)
        self.exitFullScreen.setObjectName("exitFullScreen")
        self.processMenu.addAction(self.start)
        self.processMenu.addAction(self.stop)
        self.systemMenu.addAction(self.chen1)
        self.systemMenu.addAction(self.chen2)
        self.systemMenu.addAction(self.li)
        self.systemMenu.addAction(self.yv1)
        self.systemMenu.addAction(self.yv2)
        self.systemMenu.addAction(self.wang)
        self.systemMenu.addAction(self.pan)
        self.systemMenu.addAction(self.yue)
        self.setupMenu.addAction(self.openConfigFile)
        self.viewMenu.addAction(self.fullScreen)
        self.viewMenu.addAction(self.exitFullScreen)
        self.menuBar.addAction(self.processMenu.menuAction())
        self.menuBar.addAction(self.systemMenu.menuAction())
        self.menuBar.addAction(self.viewMenu.menuAction())
        self.menuBar.addAction(self.setupMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于人工智能的生产流程分析与可视化系统"))
        self.titleLabel.setText(_translate("MainWindow", "生产流程的多维分析与可视化"))
        self.pushButton_1.setText(_translate("MainWindow", "OP30线厚度检测传感器"))
        self.pushButton_2.setText(_translate("MainWindow", "OP40线定位台传感器"))
        self.pushButton_3.setText(_translate("MainWindow", "OP30报警-今日频次"))
        self.pushButton_4.setText(_translate("MainWindow", "OP30报警-一周波形"))
        self.pushButton_5.setText(_translate("MainWindow", "萨瓦尼尼线异常事件情况"))
        self.pushButton_6.setText(_translate("MainWindow", "薄板通用线异常事件情况"))
        self.pushButton_7.setText(_translate("MainWindow", "侧板焊接线OEE能效统计"))
        self.pushButton_8.setText(_translate("MainWindow", "厚板线OEE能效统计"))
        self.processMenu.setTitle(_translate("MainWindow", "程序"))
        self.systemMenu.setTitle(_translate("MainWindow", "系统"))
        self.setupMenu.setTitle(_translate("MainWindow", "设置"))
        self.viewMenu.setTitle(_translate("MainWindow", "显示"))
        self.openConfigFile.setText(_translate("MainWindow", "打开配置文件"))
        self.start.setText(_translate("MainWindow", "启动"))
        self.stop.setText(_translate("MainWindow", "终止"))
        self.chen1.setText(_translate("MainWindow", "智能异常事件监测与保护系统"))
        self.chen2.setText(_translate("MainWindow", "产品工件智能角度检测系统"))
        self.li.setText(_translate("MainWindow", "传感器数据采集分析与可视化系统"))
        self.yv1.setText(_translate("MainWindow", "生产线报警智能检测分析系统"))
        self.yv2.setText(_translate("MainWindow", "工厂CPS产线建模与分析系统"))
        self.wang.setText(_translate("MainWindow", "工厂侧板效率智能检测系统"))
        self.pan.setText(_translate("MainWindow", "产品包装配件完整性监测系统"))
        self.yue.setText(_translate("MainWindow", "厚板线OEE效率检测系统"))
        self.fullScreen.setText(_translate("MainWindow", "全屏模式"))
        self.exitFullScreen.setText(_translate("MainWindow", "退出全屏"))