# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Documents\Data Science\pairwise_gui\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName("left_menu_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.left_menu_widget)
        self.gridLayout_2.setContentsMargins(6, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.left_menu_widget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setMinimumSize(QtCore.QSize(40, 40))
        self.label_9.setMaximumSize(QtCore.QSize(40, 40))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/icons/app_icon_dna_32.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.left_menu_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_1 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.btn_1.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/dna-helix-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_1.setIcon(icon)
        self.btn_1.setObjectName("btn_1")
        self.verticalLayout_3.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.frame_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/scatter-plot-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_2.setIcon(icon1)
        self.btn_2.setObjectName("btn_2")
        self.verticalLayout_3.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/extensions-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_3.setIcon(icon2)
        self.btn_3.setObjectName("btn_3")
        self.verticalLayout_3.addWidget(self.btn_3)
        self.btn_4 = QtWidgets.QPushButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/internet-32.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_4.setIcon(icon3)
        self.btn_4.setObjectName("btn_4")
        self.verticalLayout_3.addWidget(self.btn_4)
        self.gridLayout_2.addWidget(
            self.frame_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.frame_5 = QtWidgets.QFrame(self.left_menu_widget)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setMinimumSize(QtCore.QSize(50, 50))
        self.label_10.setMaximumSize(QtCore.QSize(50, 50))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/icons/analysis32.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(
            self.label_10, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.left_menu_widget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setContentsMargins(5, 0, 0, 4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setMinimumSize(QtCore.QSize(40, 40))
        self.label_11.setMaximumSize(QtCore.QSize(40, 40))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/images/images/web-development.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setMinimumSize(QtCore.QSize(40, 40))
        self.label_12.setMaximumSize(QtCore.QSize(40, 40))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/images/images/github.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setMinimumSize(QtCore.QSize(40, 40))
        self.label_13.setMaximumSize(QtCore.QSize(40, 40))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/images/images/paypal.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.left_menu_widget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(3, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.header_frame = QtWidgets.QFrame(self.frame_2)
        self.header_frame.setStyleSheet("")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.header_frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_btn = QtWidgets.QPushButton(self.frame_10)
        self.menu_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.menu_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/align-center.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/arrow-right-circle.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.menu_btn.setIcon(icon4)
        self.menu_btn.setIconSize(QtCore.QSize(40, 40))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_3.addWidget(self.menu_btn)
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_2.addWidget(self.frame_10, 0, QtCore.Qt.AlignLeft)
        self.frame_11 = QtWidgets.QFrame(self.header_frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(
            self.label_7, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.header_nav = QtWidgets.QFrame(self.header_frame)
        self.header_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_nav.setObjectName("header_nav")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_nav)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.min_btn = QtWidgets.QPushButton(self.header_nav)
        self.min_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.min_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.min_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/icons/icons/minus.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.min_btn.setIcon(icon5)
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout_4.addWidget(self.min_btn)
        self.max_btn = QtWidgets.QPushButton(self.header_nav)
        self.max_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.max_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.max_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/icons/icons/maximize-2.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.max_btn.setIcon(icon6)
        self.max_btn.setObjectName("max_btn")
        self.horizontalLayout_4.addWidget(self.max_btn)
        self.close_btn = QtWidgets.QPushButton(self.header_nav)
        self.close_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.close_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.close_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.close_btn.setIcon(icon7)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_4.addWidget(self.close_btn)
        self.horizontalLayout_2.addWidget(self.header_nav, 0, QtCore.Qt.AlignRight)
        self.gridLayout_3.addWidget(self.header_frame, 0, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_8)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.gridLayout_3.addWidget(self.frame_8, 1, 0, 1, 1)
        self.footer_frame = QtWidgets.QFrame(self.frame_2)
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_13 = QtWidgets.QFrame(self.footer_frame)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Lora-VariableFont")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_5.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.footer_frame)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.size_grip = QtWidgets.QFrame(self.frame_14)
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.verticalLayout.addWidget(self.size_grip)
        self.horizontalLayout_5.addWidget(
            self.frame_14, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom
        )
        self.gridLayout_3.addWidget(
            self.footer_frame, 2, 0, 1, 1, QtCore.Qt.AlignBottom
        )
        self.footer_frame.raise_()
        self.header_frame.raise_()
        self.frame_8.raise_()
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.menu_btn.toggled["bool"].connect(self.left_menu_widget.setHidden)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GENERAL TOOLS"))
        self.btn_1.setText(_translate("MainWindow", "Basic Information"))
        self.btn_2.setText(_translate("MainWindow", "Dot Plot "))
        self.btn_3.setText(_translate("MainWindow", "Local Alignment"))
        self.btn_4.setText(_translate("MainWindow", "Global Alignment"))
        self.label_2.setText(_translate("MainWindow", "ABOUT "))
        self.label_5.setText(_translate("MainWindow", "Donation"))
        self.label_3.setText(_translate("MainWindow", "Developer's Info"))
        self.label_4.setText(_translate("MainWindow", "GitHub"))
        self.label_6.setText(_translate("MainWindow", "MENU"))
        self.label_7.setText(_translate("MainWindow", "BioBytes PairSync"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Sample Tab")
        )
        self.label_8.setText(
            _translate(
                "MainWindow", "Copyright BioBytes PairSync v1.0.1 All Rights Reserved"
            )
        )
