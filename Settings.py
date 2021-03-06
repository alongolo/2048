# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Settings(QMainWindow):
    def __init__(self, parent):
        super(Settings, self).__init__(parent)
        self.setObjectName("Settings")
        self.resize(200, 202)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 131))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 181, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(290, 230, 120, 80))
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 181, 54))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ok_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(lambda: self.clicked_ok(parent))
        self.verticalLayout_2.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(lambda: self.clicked_cancel())
        self.verticalLayout_2.addWidget(self.cancel_button)
        self.widget.setObjectName("widget")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def clicked_ok(self, p):
        p.close()
        if self.radioButton_3.isChecked():
            p.__init__(6)
        elif self.radioButton_2.isChecked():
            p.__init__(4)
        elif self.radioButton.isChecked():
            p.__init__(8)
        else:
            self.close()
            return
        # p.new_game()
        p.show()
        self.close()

    def clicked_cancel(self):
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Settings", "Settings"))
        self.groupBox.setTitle(_translate("MainWindow", "Board Size"))
        self.radioButton.setText(_translate("MainWindow", "8 On 8 Tiles"))
        self.radioButton_3.setText(_translate("MainWindow", "6 On 6 Tiles"))
        self.radioButton_2.setText(_translate("MainWindow", "4 On 4 Tiles"))
        self.ok_button.setText(_translate("MainWindow", "Ok"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))


if (False):
    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
