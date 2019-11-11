# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LCD_Slider_Btn.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(442, 351)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushBtnMinus = QtWidgets.QPushButton(self.centralwidget)
		self.pushBtnMinus.setGeometry(QtCore.QRect(30, 190, 89, 25))
		self.pushBtnMinus.setObjectName("pushBtnMinus")
		self.pushBtnPlus = QtWidgets.QPushButton(self.centralwidget)
		self.pushBtnPlus.setGeometry(QtCore.QRect(270, 190, 89, 25))
		self.pushBtnPlus.setObjectName("pushBtnPlus")
		self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
		self.horizontalSlider.setGeometry(QtCore.QRect(30, 150, 321, 16))
		self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider.setObjectName("horizontalSlider")
		self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
		self.lcdNumber.setGeometry(QtCore.QRect(110, 80, 161, 51))
		self.lcdNumber.setObjectName("lcdNumber")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display)
		 
		self.pushBtnMinus.clicked.connect(self.myMinusSlot)
		self.pushBtnPlus.clicked.connect(self.myPlusSlot)
		
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	####### Selbst codierte Slots ####################	
	def myMinusSlot(self, MainWindow):
		wert = self.horizontalSlider.value()
		wert = wert-1
		self.horizontalSlider.setValue(wert)

	def myPlusSlot(self, MainWindow):
		wert = self.horizontalSlider.value()
		wert = wert+1
		self.horizontalSlider.setValue(wert)
	####################################################
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushBtnMinus.setText(_translate("MainWindow", "<"))
		self.pushBtnPlus.setText(_translate("MainWindow", ">"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

