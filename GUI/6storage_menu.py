import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import hashlib
from menu2 import Ui_menu2
from Password_storage_addition import Ui_Form
from Password_storage_view import Ui_view
from Password_storage_deletion import Ui_delete
from Password_storage_update import Ui_update


class access(QDialog):
    def addfn(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()



    def viewfn(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_view()
        self.ui.setupUi(self.window)
        self.window.show()

    def updpass(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_update()
        self.ui.setupUi(self.window)
        self.window.show()

    def deletefn(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_delete()
        self.ui.setupUi(self.window)
        self.window.show()

    def menu2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_menu2()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self):
        super(access,self).__init__()
        loadUi("C:/Users/shail/projects/pswd_pest/Password_Encryption_Sys/Final Code/accessmenudia.ui",self)

        self.setStyleSheet("background-color: #083224;")
        self.view.setStyleSheet("background-color: white")
        self.add.setStyleSheet("background-color: white")
        self.updatepass.setStyleSheet("background-color: white")
        self.delpass.setStyleSheet("background-color: white")
        self.sidelab.setStyleSheet("background-color: #f3ebeb")
        self.sidepic.setStyleSheet("background-color: #f3ebeb")

        self.accesslab.setStyleSheet("background-color: #197278")
        self.to_menu2.setStyleSheet("background-color: white")

        #NOTE
        #self.w=Password_storage_addition.Ui_Form()

        self.to_menu2.clicked.connect(self.menu2)
        self.add.clicked.connect(self.addfn)
        self.view.clicked.connect(self.viewfn)
        self.updatepass.clicked.connect(self.updpass)
        self.delpass.clicked.connect(self.deletefn)





app=QApplication(sys.argv)
mainwindow=access()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1034)
widget.setFixedHeight(834)
widget.show()
app.exec_()