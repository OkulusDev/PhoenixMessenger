from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.setFixedSize(640, 480)
        self.setWindowTitle("Phoenix Messenger Server")
        MainWindow.setStyleSheet("font: 12pt \"Roboto\"; color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setStyleSheet("padding: 5px;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ipaddr_line = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.ipaddr_line.setObjectName("ipaddr_line")
        self.horizontalLayout.addWidget(self.ipaddr_line)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 641, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("padding: 5px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.port_line = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.port_line.setObjectName("port_line")
        self.horizontalLayout_2.addWidget(self.port_line)
        self.log_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.log_text.setEnabled(False)
        self.log_text.setGeometry(QtCore.QRect(0, 100, 641, 381))
        self.log_text.setObjectName("log_text")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 60, 641, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.start_btn = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.start_btn.setContentsMargins(0, 0, 0, 0)
        self.start_btn.setObjectName("start_btn")
        self.start_server_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.start_server_btn.setObjectName("start_server_btn")
        self.start_btn.addWidget(self.start_server_btn)
        self.shutdown_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.shutdown_btn.setObjectName("shutdown_btn")
        self.start_btn.addWidget(self.shutdown_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "IP адрес"))
        self.ipaddr_line.setText(_translate("MainWindow", "127.0.0.1"))
        self.label_2.setText(_translate("MainWindow", "Порт сервера"))
        self.port_line.setText(_translate("MainWindow", "8080"))
        self.start_server_btn.setText(_translate("MainWindow", "Запустить"))
        self.shutdown_btn.setText(_translate("MainWindow", "Отключить"))
