# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_calci(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, calci):
        calci.setObjectName(_fromUtf8("calci"))
        self.setFixedSize(330, 316)
        self.seven = QtGui.QPushButton(calci)
        self.seven.setGeometry(QtCore.QRect(10, 110, 70, 40))
        self.seven.setObjectName(_fromUtf8("seven"))
        self.four = QtGui.QPushButton(calci)
        self.four.setGeometry(QtCore.QRect(10, 160, 70, 40))
        self.four.setObjectName(_fromUtf8("four"))
        self.nine = QtGui.QPushButton(calci)
        self.nine.setGeometry(QtCore.QRect(170, 110, 70, 40))
        self.nine.setObjectName(_fromUtf8("nine"))
        self.eight = QtGui.QPushButton(calci)
        self.eight.setGeometry(QtCore.QRect(90, 110, 70, 40))
        self.eight.setObjectName(_fromUtf8("eight"))
        self.six = QtGui.QPushButton(calci)
        self.six.setGeometry(QtCore.QRect(170, 160, 70, 40))
        self.six.setObjectName(_fromUtf8("six"))
        self.five = QtGui.QPushButton(calci)
        self.five.setGeometry(QtCore.QRect(90, 160, 70, 40))
        self.five.setObjectName(_fromUtf8("five"))
        self.one = QtGui.QPushButton(calci)
        self.one.setGeometry(QtCore.QRect(10, 210, 70, 40))
        self.one.setObjectName(_fromUtf8("one"))
        self.three = QtGui.QPushButton(calci)
        self.three.setGeometry(QtCore.QRect(170, 210, 70, 40))
        self.three.setObjectName(_fromUtf8("three"))
        self.two = QtGui.QPushButton(calci)
        self.two.setGeometry(QtCore.QRect(90, 210, 70, 40))
        self.two.setObjectName(_fromUtf8("two"))
        self.plus = QtGui.QPushButton(calci)
        self.plus.setGeometry(QtCore.QRect(250, 110, 70, 40))
        self.plus.setObjectName(_fromUtf8("plus"))
        self.multi = QtGui.QPushButton(calci)
        self.multi.setGeometry(QtCore.QRect(250, 210, 70, 40))
        self.multi.setObjectName(_fromUtf8("multi"))
        self.sub = QtGui.QPushButton(calci)
        self.sub.setGeometry(QtCore.QRect(250, 160, 70, 40))
        self.sub.setObjectName(_fromUtf8("sub"))
        self.dot = QtGui.QPushButton(calci)
        self.dot.setGeometry(QtCore.QRect(170, 260, 70, 40))
        self.dot.setObjectName(_fromUtf8("dot"))
        self.zero = QtGui.QPushButton(calci)
        self.zero.setGeometry(QtCore.QRect(90, 260, 71, 40))
        self.zero.setObjectName(_fromUtf8("zero"))
        self.div = QtGui.QPushButton(calci)
        self.div.setGeometry(QtCore.QRect(250, 260, 70, 40))
        self.div.setObjectName(_fromUtf8("div"))
        self.lineEdit = QtGui.QLineEdit(calci)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 310, 35))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.equal = QtGui.QPushButton(calci)
        self.equal.setGeometry(QtCore.QRect(10, 260, 70, 40))
        self.equal.setObjectName(_fromUtf8("equal"))
        self.BACK = QtGui.QPushButton(calci)
        self.BACK.setGeometry(QtCore.QRect(170, 60, 151, 40))
        self.BACK.setObjectName(_fromUtf8("BACK"))
        self.CLR = QtGui.QPushButton(calci)
        self.CLR.setGeometry(QtCore.QRect(10, 60, 151, 40))
        self.CLR.setObjectName(_fromUtf8("CLR"))

        self.retranslateUi(calci)
        QtCore.QMetaObject.connectSlotsByName(calci)

    def retranslateUi(self, calci):
        calci.setWindowTitle(_translate("calci", "Calculator", None))
        self.seven.setText(_translate("calci", "7", None))
        self.four.setText(_translate("calci", "4", None))
        self.nine.setText(_translate("calci", "9", None))
        self.eight.setText(_translate("calci", "8", None))
        self.six.setText(_translate("calci", "6", None))
        self.five.setText(_translate("calci", "5", None))
        self.one.setText(_translate("calci", "1", None))
        self.three.setText(_translate("calci", "3", None))
        self.two.setText(_translate("calci", "2", None))
        self.plus.setText(_translate("calci", "+", None))
        self.multi.setText(_translate("calci", "*", None))
        self.sub.setText(_translate("calci", "-", None))
        self.dot.setText(_translate("calci", ".", None))
        self.zero.setText(_translate("calci", "0", None))
        self.div.setText(_translate("calci", "/", None))
        self.equal.setText(_translate("calci", "=", None))
        self.BACK.setText(_translate("calci", "←", None))
        self.CLR.setText(_translate("calci", "C", None))
        self.one.clicked.connect(self.One)
        self.two.clicked.connect(self.Two)
        self.three.clicked.connect(self.Three)
        self.four.clicked.connect(self.Four)
        self.five.clicked.connect(self.Five)
        self.six.clicked.connect(self.Six)
        self.seven.clicked.connect(self.Seven)
        self.eight.clicked.connect(self.Eight)
        self.nine.clicked.connect(self.Nine)
        self.zero.clicked.connect(self.Zero)
        self.plus.clicked.connect(self.Plus)
        self.sub.clicked.connect(self.Minus)
        self.equal.clicked.connect(self.Equal)
        self.dot.clicked.connect(self.Dot)
        self.div.clicked.connect(self.BS)
        self.multi.clicked.connect(self.Asterisk)
        self.CLR.clicked.connect(self.Clr)
        self.BACK.clicked.connect(self.BSpace)


    @QtCore.pyqtSlot()
    def One(self):
        self.lineEdit.insert("1")
    @QtCore.pyqtSlot()
    def Two(self):
        self.lineEdit.insert("2")
    @QtCore.pyqtSlot()
    def Three(self):
        self.lineEdit.insert("3")
    @QtCore.pyqtSlot()
    def Four(self):
        self.lineEdit.insert("4")
    @QtCore.pyqtSlot()
    def Five(self):
        self.lineEdit.insert("5")
    @QtCore.pyqtSlot()
    def Six(self):
        self.lineEdit.insert("6")
    @QtCore.pyqtSlot()
    def Seven(self):
        self.lineEdit.insert("7")
    @QtCore.pyqtSlot()
    def Eight(self):
        self.lineEdit.insert("8")
    @QtCore.pyqtSlot()
    def Nine(self):
        self.lineEdit.insert("9")
    @QtCore.pyqtSlot()
    def Zero(self):
        self.lineEdit.insert("0")
    @QtCore.pyqtSlot()
    def Plus(self):
        count = 0
        txt = self.lineEdit.displayText()
        for letter in txt:
        	count = count + 1
        if (txt[count-1]!='+' and txt[count-1]!='-' and txt[count-1]!='*' and txt[count-1]!='/'):
        	self.lineEdit.insert("+")
    @QtCore.pyqtSlot()
    def Minus(self):
    	count = 0
        txt = self.lineEdit.displayText()
        for letter in txt:
        	count = count + 1
        if (txt[count-1]!='+' and txt[count-1]!='-' and txt[count-1]!='*' and txt[count-1]!='/'):
        	self.lineEdit.insert("-")
    @QtCore.pyqtSlot()
    def Equal(self):
        self.lineEdit.insert("=")
    @QtCore.pyqtSlot()
    def Dot(self):
    	count = 0
    	d = 0
        txt = self.lineEdit.displayText()
        for letter in txt:
        	count = count + 1
        	if letter == '.':
        		d=d+1
        	if letter =='+' or letter == '-' or letter == '*' or letter == '/':
        		d=0
        if txt[count-1]!='.' and d<1:
        	self.lineEdit.insert(".")
    @QtCore.pyqtSlot()
    def BS(self):
    	count = 0
        txt = self.lineEdit.displayText()
        for letter in txt:
        	count = count + 1
        if (txt[count-1]!='+' and txt[count-1]!='-' and txt[count-1]!='*' and txt[count-1]!='/'):
        	self.lineEdit.insert("/")
    @QtCore.pyqtSlot()
    def Asterisk(self):
    	count = 0
        txt = self.lineEdit.displayText()
        for letter in txt:
        	count = count + 1
        if (txt[count-1]!='+' and txt[count-1]!='-' and txt[count-1]!='*' and txt[count-1]!='/'):
        	self.lineEdit.insert("*")

    def Clr(self):
        self.lineEdit.clear()

    def BSpace(self):
        self.lineEdit.backspace()

    def Equal(self):
	    txt = self.lineEdit.displayText()
	    res = eval(str(txt))
	    self.lineEdit.clear()
	    self.lineEdit.insert(str(res))
       

def run():
    app = QtGui.QApplication(sys.argv)
    ex = Ui_calci()
    ex.show()
    sys.exit(app.exec_())

run()



