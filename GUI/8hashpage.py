import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import hashlib
from menu2 import Ui_menu2


class hash(QDialog):
    def openwin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_menu2()
        self.ui.setupUi(self.window)
        self.window.show()
    def __init__(self):
        super(hash,self).__init__()
        loadUi("C:/Users/shail/projects/pswd_pest/Password_Encryption_Sys/Final Code/hashpagedia.ui",self)

        self.setStyleSheet("background-color: #083224;")
        self.sha1_5.setStyleSheet("background-color: white")
        self.sha256_5.setStyleSheet("background-color: white")
        self.md5_5.setStyleSheet("background-color: white")
        self.hashlabel_5.setStyleSheet("background-color: #197278")
        self.enterpass_5.setStyleSheet("background-color: #c44536")
        self.hashed_password_5.setStyleSheet("background-color: #c44536")
        self.to_menu2.setStyleSheet("background-color: white")



        self.to_menu2.clicked.connect(self.openwin)
        self.sha1_5.clicked.connect(self.sha_1)
        self.sha256_5.clicked.connect(self.sha_256)
        self.md5_5.clicked.connect(self.md_5)


    def sha_1(self):
        password_input=self.password_input_5.toPlainText()
        hash_obj=hashlib.sha1()
        hash_obj.update(password_input.encode())
        self.hashpass=hash_obj.hexdigest()
        print(self.hashpass)
        self.hashed_input_5.setText(self.hashpass)
        self.hashed_input_5.adjustSize()

    def sha_256(self):
        password_input=self.password_input_5.toPlainText()
        hash_obj=hashlib.sha256()
        hash_obj.update(password_input.encode())
        self.hashpass=hash_obj.hexdigest()
        print(self.hashpass)
        self.hashed_input_5.setText(self.hashpass)
        self.hashed_input_5.adjustSize()

    def md_5(self):
        password_input=self.password_input_5.toPlainText()
        hash_obj=hashlib.md5()
        hash_obj.update(password_input.encode())
        self.hashpass=hash_obj.hexdigest()
        print(self.hashpass)
        self.hashed_input_5.setText(self.hashpass)
        self.hashed_input_5.adjustSize()



app=QApplication(sys.argv)
mainwindow=hash()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1034)
widget.setFixedHeight(834)
widget.show()
app.exec_()