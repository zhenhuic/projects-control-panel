# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Lab417\projects-control-panel\panel_gui\control_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from panel_gui.cunstom_widgets import ClickableLabel


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
"color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);")
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1263, 1249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        # self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_1 = ClickableLabel(self.scrollAreaWidgetContents)
        self.label_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMinimumSize(QtCore.QSize(551, 320))
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_1.setSizeIncrement(QtCore.QSize(1, 1))
        self.label_1.setBaseSize(QtCore.QSize(1, 1))
        self.label_1.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        # self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3 = ClickableLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(551, 300))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_3.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        # self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2 = ClickableLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(551, 320))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.label_2.setBaseSize(QtCore.QSize(1, 1))
        self.label_2.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_2.setText("")
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        # self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5 = ClickableLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(551, 300))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_5.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        # self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6 = ClickableLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(551, 300))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_6.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        # self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4 = ClickableLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(551, 300))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_4.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        # self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7 = ClickableLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(551, 300))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_7.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        # self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8 = ClickableLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(551, 300))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 350))
        self.label_8.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 14)
        self.horizontalLayout.setStretch(2, 1)
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
        self.titleLabel.setText(_translate("MainWindow", "基于人工智能的生产流程分析与可视化系统"))
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
