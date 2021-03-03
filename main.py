# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 520)
        MainWindow.setMinimumSize(QtCore.QSize(600, 520))
        MainWindow.setMaximumSize(QtCore.QSize(600, 520))
        MainWindow.setStyleSheet("font: 12pt \"Intro Regular Alt\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 591, 861))
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 581, 471))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 579, 469))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 578, 256))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("font: 75 14pt \"Intro Bold Alt\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 75 14pt \"Intro Book Alt\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("font: 75 14pt \"Intro Book Alt\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setStyleSheet("background: rgba(255,255,255,0.5);\n"
                                      "font: 20pt \"Intro Regular Caps\";\n"
                                      "padding: 15px 30px;\n"
                                      "color: rgba(30, 255, 188, 1);\n"
                                      "border:2px solid  rgb(214, 48, 48);\n"
                                      "border-bottom-width: 2px;\n"
                                      "border-bottom-width: 4px;\n"
                                      "color: rgb(214, 48, 48);\n"
                                      "border-radius: 5px;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("font: 75 14pt \"Intro Bold Alt\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("font: 87 16pt \"Intro Black Caps\";\n"
                                 "color: rgb(37, 37, 37);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 87 16pt \"Intro Black Alt\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("font: 75 14pt \"Intro Bold Alt\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("font: 75 14pt \"Intro Book Alt\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setStyleSheet("font: 75 14pt \"Intro Bold Alt\";")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 4, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setStyleSheet("font: 75 14pt \"Intro Bold Alt\";")
        self.label_14.setObjectName("label_14")

        # TAB 2
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 571, 471))
        self.scrollArea.setMinimumSize(QtCore.QSize(571, 471))
        self.scrollArea.setMaximumSize(QtCore.QSize(580, 1471))
        self.scrollArea.setBaseSize(QtCore.QSize(571, 471))
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setTabletTracking(False)
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(6, -327, 540, 796))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(540, 1600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setContentsMargins(1, -1, -1, -1)
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 4, 0, 1, 2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_3.addWidget(self.checkBox_5, 16, 2, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_41.setObjectName("label_41")
        self.gridLayout_3.addWidget(self.label_41, 15, 0, 1, 2)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 7, 0, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_36.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_36.setObjectName("label_36")
        self.gridLayout_3.addWidget(self.label_36, 11, 0, 1, 2)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 8, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 7, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 9, 2, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_4, 10, 2, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_44.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 18, 0, 1, 2)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setStyleSheet("font: 87 16pt \"Intro Black Alt\";")
        self.label_40.setObjectName("label_40")
        self.gridLayout_3.addWidget(self.label_40, 14, 0, 1, 3)
        self.comboBox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_6, 19, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBox_2 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 8, 2, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_45.setStyleSheet("font: 87 20pt \"Intro Black Caps\";")
        self.label_45.setObjectName("label_45")
        self.gridLayout_3.addWidget(self.label_45, 21, 0, 1, 3)
        self.spinBox_3 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_3.addWidget(self.spinBox_3, 12, 2, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 5, 2, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_42.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_42.setObjectName("label_42")
        self.gridLayout_3.addWidget(self.label_42, 16, 0, 1, 2)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_3.addWidget(self.checkBox_6, 17, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 15, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 6, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 3)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setStyleSheet("font: 13pt \"Intro Book Alt\";")
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 2, 0, 1, 2)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_3.addWidget(self.checkBox_7, 18, 2, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 11, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 5, 0, 1, 2)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_46.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_46.setObjectName("label_46")
        self.gridLayout_3.addWidget(self.label_46, 19, 0, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setStyleSheet("font: 13pt \"Intro Book Alt\";")
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 3, 0, 1, 2)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 9, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 100))
        self.pushButton_3.setStyleSheet("background: rgba(255,255,255,0.5);\n"
                                        "font: 20pt \"Intro Regular Caps\";\n"
                                        "padding: 15px 30px;\n"
                                        "color: rgba(30, 255, 188, 1);\n"
                                        "border:2px solid  rgb(214, 48, 48);\n"
                                        "border-bottom-width: 2px;\n"
                                        "border-bottom-width: 4px;\n"
                                        "color: rgb(214, 48, 48);\n"
                                        "border-radius: 5px;\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 20, 0, 1, 3)
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_49.setStyleSheet("font: 14pt \"Intro Regular Alt\";")
        self.label_49.setObjectName("label_49")
        self.gridLayout_3.addWidget(self.label_49, 23, 0, 1, 3)
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_43.setStyleSheet("font: 12pt \"Intro Book Alt\";")
        self.label_43.setObjectName("label_43")
        self.gridLayout_3.addWidget(self.label_43, 17, 0, 1, 2)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_38.setObjectName("label_38")
        self.gridLayout_3.addWidget(self.label_38, 13, 0, 1, 2)
        self.spinBox_4 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_3.addWidget(self.spinBox_4, 13, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 6, 0, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setStyleSheet("font: 87 16pt \"Intro Black Caps\";\n"
                                    "color: rgb(37, 37, 37);")
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 10, 0, 1, 2)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_37.setStyleSheet("font: 14pt \"Intro Book Alt\";")
        self.label_37.setObjectName("label_37")
        self.gridLayout_3.addWidget(self.label_37, 12, 0, 1, 2)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setStyleSheet("font: 87 16pt \"Intro Black Alt\";")
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 0, 1, 1, 2)
        self.graphicsView = QtWidgets.QLabel(self.scrollAreaWidgetContents, )
        self.pixmap = QPixmap("img/interview.png")
        self.graphicsView.setPixmap(self.pixmap)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 22, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_47.setStyleSheet("font: 87 20pt \"Intro Black Caps\"; text-align:center;")
        self.label_47.setObjectName("label_47")
        self.gridLayout_3.addWidget(self.label_47, 22, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моделювання бізнес задач процесів кредитного відділу банку"))
        self.label_9.setText(_translate("MainWindow", "Місячний платіж:"))
        self.label_11.setText(_translate("MainWindow", "___"))
        self.label_3.setText(_translate("MainWindow", "Сума кредиту:"))
        self.label_12.setText(_translate("MainWindow", "___"))
        self.label_4.setText(_translate("MainWindow", "Відсоток:"))
        self.pushButton.setText(_translate("MainWindow", "Розрахувати"))
        self.label_10.setText(_translate("MainWindow", "Плата за весь первіод:"))
        self.label.setText(_translate("MainWindow", "Задачі 1,2"))
        self.label_2.setText(_translate("MainWindow", "Річний і місячний розрахунок по кредиту"))
        self.label_6.setText(_translate("MainWindow", "грн."))
        self.label_5.setText(_translate("MainWindow", "Період:"))
        self.doubleSpinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "%"))
        self.label_14.setText(_translate("MainWindow", "років"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Задачі 1,2"))
        self.label_29.setText(_translate("MainWindow", "Документи є валідними"))
        self.label_41.setText(_translate("MainWindow", "Підозрілість клієнта"))
        self.label_32.setText(_translate("MainWindow", "Сімейний стан"))
        self.label_36.setText(_translate("MainWindow", "Сфера діяльності"))
        self.label_33.setText(_translate("MainWindow", "Кількість дітей"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Неодружений (Незаміжня)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Одружений (Одружена)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Одружений, але живе окремо"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Розлучений (а)"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Вдівець (Вдова)"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Немає"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Середня незакінчена"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Середня спеціальна"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Середня"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Вища незакінчена"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Повна вища"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Немає"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Допоміжний персонал"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Фахівець"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Службовець"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Керівний працівник"))
        self.label_44.setText(_translate("MainWindow", "Видуманні данні"))
        self.label_40.setText(_translate("MainWindow", "Особливості"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Немає"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Погана"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Добра"))
        self.label_45.setText(_translate("MainWindow", "Висновки"))
        self.label_42.setText(_translate("MainWindow", "Займ не на себе"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Чоловіча"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Жіноча"))
        self.label_27.setText(_translate("MainWindow", "Паспорт громадянина України"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Безробітний"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Студент"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Пенсіонер"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Держ. служба"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Приватний сектор"))
        self.label_30.setText(_translate("MainWindow", "Вік позичальника"))
        self.label_46.setText(_translate("MainWindow", "Кредитна історія"))
        self.label_28.setText(_translate("MainWindow", "Наявність інших документів"))
        self.label_34.setText(_translate("MainWindow", "Освіта"))
        self.pushButton_3.setText(_translate("MainWindow", "Розрахувати"))
        self.label_49.setText(_translate("MainWindow", "___"))
        self.label_43.setText(_translate("MainWindow", "Неадекватний стан позичальника"))
        self.label_38.setText(_translate("MainWindow", "Середньомісячний дохід"))
        self.label_31.setText(_translate("MainWindow", "Стать"))
        self.label_26.setText(_translate("MainWindow", "Задача 3"))
        self.label_35.setText(_translate("MainWindow", "Кваліфікація"))
        self.label_37.setText(_translate("MainWindow", "Cтаж роботи"))
        self.label_25.setText(_translate("MainWindow", "Кредитний скоринг"))
        self.label_47.setText(_translate("MainWindow", "---"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Задача 3"))
        # LOGIC
        self.doubleSpinBox.setRange(1, 1000000)
        self.doubleSpinBox.setValue(1)
        self.doubleSpinBox_2.setRange(1, 1000000)
        self.doubleSpinBox_2.setValue(1)
        self.doubleSpinBox_3.setRange(1, 1000000)
        self.doubleSpinBox_3.setValue(1)
        self.spinBox_4.setRange(1000, 10000000)
        self.spinBox_4.setValue(1000)

        def getResult1(event):
            """
            Функція отримання місячного та загального платежу
            n - сума кредиту (грн.)
            y - період (роки)
            p - відсоток (%)
            """
            n = self.doubleSpinBox.value()
            p = self.doubleSpinBox_2.value()
            y = self.doubleSpinBox_3.value()
            p = p / 100
            month_pay = (n * p * (1 + p) ** y) / (12 * ((1 + p) ** y - 1))
            monthPayFinal = round(month_pay, 2)
            self.label_11.setText(str(monthPayFinal) + " грн.")
            summa = month_pay * y * 12
            summaFinal = round(summa, 2)
            self.label_12.setText(str(summaFinal) + " грн.")
            self.label_11.setStyleSheet("font-style: italic;\n"
                                        "color: rgb(0, 170, 42);\n")
            self.label_12.setStyleSheet("font-style: italic;\n"
                                        "color: rgb(0, 170, 42);\n")

        self.pushButton.clicked.connect(getResult1)

        def getResult2():
            score = 0
            # PASSPORT ::check
            if not self.checkBox.isChecked():
                score = -800
            # DOCUMENTS ::check
            if not self.checkBox_2.isChecked():
                score = -800
            # DOCUMENTS VALIDATION ::check
            if not self.checkBox_3.isChecked():
                score = -800
            # AGE ::check
            if self.spinBox.value() <= 17:
                score -= 800
            elif 18 <= self.spinBox.value() <= 20:
                score += 20
            elif 21 <= self.spinBox.value() <= 25:
                score += 38
            elif 26 <= self.spinBox.value() <= 30:
                score += 70
            elif 31 <= self.spinBox.value() <= 35:
                score += 82
            elif 36 <= self.spinBox.value() <= 50:
                score += 95
            elif 51 <= self.spinBox.value() <= 60:
                score += 110
            else:
                score += 25
            # SEX ::check
            if self.comboBox_2.currentText() == "Чоловіча":
                score += 20
            else:
                score += 25
            # MARITAL STATUS ::check
            if self.comboBox.currentText() == "Неодружений (Незаміжня)":
                score += 110
            elif self.comboBox.currentText() == "Одружений (Одружена)":
                score += 150
            elif self.comboBox.currentText() == "Одружений, але живе окремо":
                score += 65
            elif self.comboBox.currentText() == "Розлучений (а)":
                score += 90
            elif self.comboBox.currentText() == "Вдівець (Вдова)":
                score += 85
            else:
                score += 10
            # KIDS COUNT ::check
            if self.spinBox_2.value() == 0:
                score += 100
            elif self.spinBox_2.value() == 1:
                score += 75
            elif self.spinBox_2.value() == 2:
                score += 55
            elif self.spinBox_2.value() == 3:
                score += 30
            elif self.spinBox_2.value() >= 4:
                score += 10
            else:
                score += 10
            # EDUCATION ::check
            if self.comboBox_3.currentText() == "Немає":
                score += 10
            elif self.comboBox_3.currentText() == "Середня незакінчена":
                score += 15
            elif self.comboBox_3.currentText() == "Середня спеціальна":
                score += 28
            elif self.comboBox_3.currentText() == "Середня":
                score += 22
            elif self.comboBox_3.currentText() == "Вища незакінчена":
                score += 32
            elif self.comboBox_3.currentText() == "Повна вища":
                score += 40
            else:
                score += 10
            # QUALIFICATION ::check
            if self.comboBox_4.currentText() == "Немає":
                score += 10
            elif self.comboBox_4.currentText() == "Допоміжний персонал":
                score += 35
            elif self.comboBox_4.currentText() == "Фахівець":
                score += 85
            elif self.comboBox_4.currentText() == "Службовець":
                score += 100
            elif self.comboBox_4.currentText() == "Керівний працівник":
                score += 140
            else:
                score += 10
            # FIELD OF ACTIVITY ::check
            if self.comboBox_5.currentText() == "Безробітний":
                score += 10
            elif self.comboBox_5.currentText() == "Студент":
                score += 80
            elif self.comboBox_5.currentText() == "Пенсіонер":
                score += 30
            elif self.comboBox_5.currentText() == "Держ. служба":
                score += 110
            elif self.comboBox_5.currentText() == "Приватний сектор":
                score += 170
            else:
                score += 10
            # EXPERIENCE ::check
            if self.spinBox_3.value() < 1:
                score += 20
            elif 1 < self.spinBox_3.value() < 2:
                score += 40
            elif 2 < self.spinBox_3.value() < 3:
                score += 65
            elif 3 < self.spinBox_3.value() < 5:
                score += 90
            elif self.spinBox_3.value() > 5:
                score += 130
            else:
                score += 10
            # INCOME ::check
            if self.spinBox_4.value() < 1000:
                score += 15
            elif 1000 < self.spinBox_4.value() < 3000:
                score += 65
            elif 3000 < self.spinBox_4.value() < 5000:
                score += 110
            elif 5000 < self.spinBox_4.value() < 10000:
                score += 190
            elif self.spinBox_4.value() >= 10000:
                score += 210
            else:
                score += 10
            # FISHILY ::check
            if self.checkBox_4.isChecked():
                score -= 800
            # OWNER ::check
            if self.checkBox_5.isChecked():
                score -= 300
            # ADEQUATE ::check
            if self.checkBox_6.isChecked():
                score -= 400
            # NOT FAKE DATA ::check
            if self.checkBox_7.isChecked():
                score -= 700
            # CREDIT STORY ::check
            if self.comboBox_6.currentText() == "Немає":
                score += 5
            elif self.comboBox_6.currentText() == "Погана":
                score -= 300
            elif self.comboBox_6.currentText() == "Добра":
                score += 100
            else:
                score += 10
            # RESULT
            result = None
            titleStyle = "font: 87 20pt \"Intro Black Caps\";"
            descriptStyle = "font: 87 20pt \"Intro Regular Alt\";"
            resultsList = {"no": ["Кредит не схвалено",
                                  "Оскільки вимоги для його надання не були виконані.",
                                  titleStyle + "color: #c4101d",
                                  descriptStyle + "color: #ab0e19",
                                  QPixmap("img/no.png")],
                           "bad": ["Кредит схвалено на поганих умовах",
                                   "Кредит на максимально невигдіних умовах для позичальника. Відсутність "
                                   "вибору кредитних планів та карт, високі відсотки",
                                   titleStyle + "color: #cc2210",
                                   descriptStyle + "color: #ad1c0c",
                                   QPixmap("img/bad.png")],
                           "fair": ["Кредит схвалено на справедливих умовах",
                                    "Кредит схвалено на невигідних умовах для позичальника. Обмежений вибір кредитних "
                                    "планів та карт, високі відсотки",
                                    titleStyle + "color: #f2c50f",
                                    descriptStyle + "color: #dbb20d",
                                    QPixmap("img/fair.png")],
                           "good": ["Кредит схвалено на вигідних умовах",
                                    "Широкий вибір кредитних планів та карт, більш низькі відсоткові ставки.",
                                    titleStyle + "color: #5aad23",
                                    descriptStyle + "color: #43821a",
                                    QPixmap("img/good.png")],
                           "excellent": ["Кредит схвалено на відмінних умовах",
                                         "Відкритий доступ до більшості переваг: низькі відсоткові ставки, великий вибір "
                                         "карт.",
                                         titleStyle + "color: #13ba9b",
                                         descriptStyle + "color: #119e84",
                                         QPixmap("img/excellent.png")],
                           "galacticError": ["Кредит не може бути схвалено, оскільки галактика зламалась",
                                             "На жаль ви зламали галактику,  вийшовши за межі заданого діапазону, "
                                             "тепер кредит вам більше не потрібен",
                                             titleStyle + "color: #24e0be",
                                             descriptStyle + "color: #08a689",
                                             QPixmap("img/goose.png")]
                           }
            if score < 300:
                result = resultsList["no"]
            elif 300 < score < 629:
                result = resultsList["bad"]
            elif 630 < score < 689:
                result = resultsList["fair"]
            elif 690 < score < 719:
                result = resultsList["good"]
            elif score > 720:
                result = resultsList["excellent"]
            else:
                result = resultsList["galacticError"]

            self.label_47.setText(result[0])
            self.label_49.setText(result[1])
            self.label_47.setWordWrap(True)
            self.label_49.setWordWrap(True)
            self.label_47.setStyleSheet(result[2])
            self.label_49.setStyleSheet(result[3])
            self.graphicsView.setPixmap(result[4])

        self.pushButton_3.clicked.connect(getResult2)
        self.statusbar.setWindowIcon(QIcon('ico.ico'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
