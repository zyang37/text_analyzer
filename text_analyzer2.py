# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzer2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from transformers import pipeline

class Ui_MainWindow(object):

    def __init__(self):
        self.answer_nlp = None
        self.summarizer_nlp = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AnswerB = QtWidgets.QPushButton(self.centralwidget)
        self.AnswerB.setGeometry(QtCore.QRect(520, 390, 181, 61))
        self.AnswerB.setObjectName("AnswerB")
        self.SummarizeB = QtWidgets.QPushButton(self.centralwidget)
        self.SummarizeB.setGeometry(QtCore.QRect(520, 10, 181, 61))
        self.SummarizeB.setObjectName("SummarizeB")
        self.ClearB = QtWidgets.QPushButton(self.centralwidget)
        self.ClearB.setGeometry(QtCore.QRect(110, 500, 191, 61))
        self.ClearB.setObjectName("ClearB")
        self.text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(0, 0, 411, 491))
        self.text.setBackgroundVisible(False)
        self.text.setObjectName("text")
        self.min = QtWidgets.QSpinBox(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(450, 10, 48, 24))
        self.min.setMaximum(500)
        self.min.setProperty("value", 50)
        self.min.setObjectName("min")
        self.max = QtWidgets.QSpinBox(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(450, 40, 48, 24))
        self.max.setMaximum(1000)
        self.max.setProperty("value", 150)
        self.max.setObjectName("max")
        self.Summary = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Summary.setGeometry(QtCore.QRect(430, 70, 361, 241))
        self.Summary.setObjectName("Summary")
        self.Question = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(430, 320, 361, 61))
        self.Question.setObjectName("Question")
        self.Answer = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Answer.setGeometry(QtCore.QRect(430, 450, 361, 101))
        self.Answer.setObjectName("Answer")
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
        self.SummarizeB.clicked.connect(self.get_summary)
        self.AnswerB.clicked.connect(self.get_answer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AnswerB.setText(_translate("MainWindow", "Answer"))
        self.SummarizeB.setText(_translate("MainWindow", "Summarize"))
        self.ClearB.setText(_translate("MainWindow", "Clear"))
        self.Summary.setPlainText(_translate("MainWindow", "Summary"))
        self.Question.setPlainText(_translate("MainWindow", "Question"))
        self.Answer.setPlainText(_translate("MainWindow", "Answer"))

    def clear_text(self):
        self.text.setPlainText("")
        self.Summary.setPlainText("Summary")
        self.Question.setPlainText("Question")
        self.Answer.setPlainText("Answer")
        self.Article = ""

    def get_summary(self):
        if self.summarizer_nlp==None:
            self.summarizer_nlp = pipeline("summarization")
        self.Article = self.text.toPlainText()
        if self.Article=="":
            self.Summary.setPlainText("no content")
        else:
            s_dict = self.summarizer_nlp(self.Article, max_length=self.max.value(), min_length=self.min.value())
            try:
                self.Summary.setPlainText(s_dict[0]['summary_text'])
            except:
                self.Summary.setPlainText("Read it yourself!!!")

    def get_answer(self):
        if self.answer_nlp==None:
            self.answer_nlp = pipeline("question-answering")

        self.q = self.Question.toPlainText()
        self.Article = self.text.toPlainText()

        if self.Article=="" or self.q=="Question":
            self.Answer.setPlainText("no text or question")
        else:
            a = self.answer_nlp(question=self.q, context=self.Article)
            try:
                self.Answer.setPlainText("{}\n\nscore: {}".format(a['answer'], str(a['score'])))
            except:
                self.Answer.setPlainText("no answer")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
