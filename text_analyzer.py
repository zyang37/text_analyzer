# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 0, 391, 501))
        self.text.setClearButtonEnabled(False)
        self.text.setObjectName("text")
        self.Summary = QtWidgets.QLabel(self.centralwidget)
        self.Summary.setGeometry(QtCore.QRect(430, 80, 341, 231))
        self.Summary.setObjectName("Summary")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(430, 450, 341, 91))
        self.answer.setObjectName("answer")
        self.question = QtWidgets.QLineEdit(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(430, 330, 341, 51))
        self.question.setObjectName("question")
        self.answerB = QtWidgets.QPushButton(self.centralwidget)
        self.answerB.setGeometry(QtCore.QRect(510, 390, 181, 61))
        self.answerB.setObjectName("answerB")
        self.SummarizeB = QtWidgets.QPushButton(self.centralwidget)
        self.SummarizeB.setGeometry(QtCore.QRect(510, 10, 181, 61))
        self.SummarizeB.setObjectName("SummarizeB")
        self.ClearB = QtWidgets.QPushButton(self.centralwidget)
        self.ClearB.setGeometry(QtCore.QRect(110, 500, 191, 61))
        self.ClearB.setObjectName("ClearB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # functions 
        self.ClearB.clicked.connect(self.clear_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Summary.setText(_translate("MainWindow", "Summary"))
        self.answer.setText(_translate("MainWindow", "Answer"))
        self.answerB.setText(_translate("MainWindow", "Answer"))
        self.SummarizeB.setText(_translate("MainWindow", "Summarize"))
        self.ClearB.setText(_translate("MainWindow", "Clear"))

    def clear_text(self):
        self.text.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
