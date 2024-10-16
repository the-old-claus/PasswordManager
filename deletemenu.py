from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QDialog
from PyQt5.QtGui import QFont, QPalette, QColor
import sys
import os
import pickle


def delete_password(pickle_file_path, website):
    try:
        with open(pickle_file_path, 'rb') as file:
            existing_data = pickle.load(file)
    except FileNotFoundError:
        existing_data = []

    updated_data = [item for item in existing_data if item['Website'] != website]

    with open(pickle_file_path, 'wb') as file:
        pickle.dump(updated_data, file)

class DeletePasswordWindow(QWidget):
    def __init__(self, pickle_file_path):
        super().__init__()
        self.pickle_file_path = pickle_file_path
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Heading
        self.label = QLabel('Password Encryption System')
        self.label.setFont(QFont('Sylfaen', 20))
        self.label.setStyleSheet("color: #F3EBEB")
        layout.addWidget(self.label)

        # Subtext - Website
        self.websiteLabel = QLabel('Website')
        self.websiteLabel.setFont(QFont('Sylfaen', 18))
        self.websiteLabel.setStyleSheet("color: #F3EBEB")
        layout.addWidget(self.websiteLabel)

        # Text Field for Website Input
        self.websiteInput = QLineEdit()
        self.websiteInput.setFixedWidth(300)
        layout.addWidget(self.websiteInput)

        # Delete Button with Red Color (#C44536)
        self.deleteButton = QPushButton('Delete')
        self.deleteButton.setStyleSheet("background-color: #C44536; color: white; font-size: 18px;")
        layout.addWidget(self.deleteButton)

        self.deleteButton.clicked.connect(self.delete_button_clicked)

        # Back Button with same styling as Delete Button
        self.backButton = QPushButton('Back')
        self.backButton.setStyleSheet("background-color: #C44536; color: white; font-size: 18px;")
        layout.addWidget(self.backButton)
        self.backButton.clicked.connect(self.back_button_clicked)

        # Set Layout and Window Properties
        self.setLayout(layout)
        self.setGeometry(100, 100, 1034, 834)
        self.setWindowTitle('Delete Password')

        # Set Background Color to Green (#083224)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#083224"))
        self.setPalette(palette)

    def delete_button_clicked(self):
        website = self.websiteInput.text()
        delete_password(self.pickle_file_path, website)
        self.websiteInput.clear()

    # Inside the DeletePasswordWindow class
    def back_button_clicked(self):
        from 6storage_menu import access
        access_instance = access()  
        access_instance.menu2()  
        self.close()  




app = QApplication(sys.argv)

pickle_file_path = os.path.join('C:', 'Users', 'shres', 'OneDrive', 'Desktop', 'Py Syntax', 'Book1.pkl')

deletePasswordWindow = DeletePasswordWindow(pickle_file_path)
deletePasswordWindow.setFixedWidth(1034)
deletePasswordWindow.setFixedHeight(834)

deletePasswordWindow.show()

sys.exit(app.exec_())