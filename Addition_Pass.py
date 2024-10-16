from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Password
import Password_2


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(997, 674)




        self.Add = QtWidgets.QPushButton(Form)
        self.Add.setGeometry(QtCore.QRect(270, 490, 93, 28))




        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 490, 93, 28))




        self.User = QtWidgets.QLabel(Form)
        self.User.setGeometry(QtCore.QRect(130, 220, 141, 31))

        self.User.setFont(QFont('Arial' , 10))



        self.Password = QtWidgets.QLabel(Form)
        self.Password.setGeometry(QtCore.QRect(130, 330, 141, 21))

        self.Password.setFont(QFont('Arial' , 10))



        self.User_in = QtWidgets.QLineEdit(Form)
        self.User_in.setGeometry(QtCore.QRect(310, 210, 481, 41))



        self.Pass_in = QtWidgets.QLineEdit(Form)
        self.Pass_in.setGeometry(QtCore.QRect(313, 310, 481, 41))



        self.Add.clicked.connect(self.addition)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Add.setText(_translate("Form", "Add"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.User.setText(_translate("Form", "User Name"))
        self.Password.setText(_translate("Form", "Password"))


    def addition(self, Form):
        textboxValue = self.Pass_in.text()
        a = Password.encrypt(textboxValue)
        user = self.User_in.text()
        Password_2.add(user, a)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())