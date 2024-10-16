from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QPalette, QColor
import sys

class UpdatePasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def back_button_clicked(self): 
        from 6storage_menu import access
        access_instance = access()
        access_instance.menu2()
        self.close()


    def initUI(self):
        layout = QVBoxLayout()


        self.label = QLabel('Password Encryption System')
        self.label.setFont(QFont('Sylfaen', 20))
        self.label.setStyleSheet("color: #F3EBEB")
        layout.addWidget(self.label)


        self.websiteLabel = QLabel('Website')
        self.websiteLabel.setFont(QFont('Sylfaen', 18))
        self.websiteLabel.setStyleSheet("color: #F3EBEB")
        layout.addWidget(self.websiteLabel)


        self.websiteInput = QLineEdit()
        self.websiteInput.setFixedWidth(300)
        layout.addWidget(self.websiteInput)


        self.newPasswordLabel = QLabel('New Password')
        self.newPasswordLabel.setFont(QFont('Sylfaen', 18))
        self.newPasswordLabel.setStyleSheet("color: #F3EBEB")
        layout.addWidget(self.newPasswordLabel)


        self.newPasswordInput = QLineEdit()
        self.newPasswordInput.setFixedWidth(300)
        layout.addWidget(self.newPasswordInput)


        self.updateButton = QPushButton('Update')
        self.updateButton.setStyleSheet("background-color: #C44536; color: white; font-size: 18px;")
        layout.addWidget(self.updateButton)

        self.updateButton.clicked.connect(lambda: update_password(pickle_file_path, self.websiteInput.text(), self.newPasswordInput.text()))


        self.setLayout(layout)
        self.setGeometry(100, 100, 1034, 834) 
        self.setWindowTitle('Update Password')

        self.backButton = QPushButton('Back')
        self.backButton.setStyleSheet("background-color: #C44536; color: white; font-size: 18px;")
        layout.addWidget(self.backButton)
        self.backButton.clicked.connect(self.back_button_clicked)



        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#083224"))
        self.setPalette(palette)


app = QApplication(sys.argv)

updatePasswordWindow = UpdatePasswordWindow()

updatePasswordWindow.show()

sys.exit(app.exec_())
