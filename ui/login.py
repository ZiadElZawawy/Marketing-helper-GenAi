import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window settings
        self.setWindowTitle('Login')
        self.setGeometry(300, 300, 300, 200)  # x, y, width, height

        # Create layout
        layout = QVBoxLayout()

        # Email field
        self.emailLabel = QLabel('Email:')
        self.emailField = QLineEdit()
        self.emailField.setPlaceholderText('Enter your email')
        layout.addWidget(self.emailLabel)
        layout.addWidget(self.emailField)

        # Password field
        self.passwordLabel = QLabel('Password:')
        self.passwordField = QLineEdit()
        self.passwordField.setPlaceholderText('Enter your password')
        self.passwordField.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordField)

        # Buttons
        buttonsLayout = QHBoxLayout()
        self.signInButton = QPushButton('Sign In')
        self.signUpButton = QPushButton('Sign Up')
        buttonsLayout.addWidget(self.signInButton)
        buttonsLayout.addWidget(self.signUpButton)
        layout.addLayout(buttonsLayout)

        # Connect buttons to functions
        self.signInButton.clicked.connect(self.signIn)
        self.signUpButton.clicked.connect(self.signUp)

        self.setLayout(layout)

    def signIn(self):
        # Placeholder for sign-in functionality
        email = self.emailField.text()
        password = self.passwordField.text()
        # Here you should check the email and password validity
        # For now, just display a message box
        QMessageBox.information(self, 'Login', 'Sign In clicked.\nEmail: {}\nPassword: {}'.format(email, password))
        # Here you would transition to the main menu UI

    def signUp(self):
        # Placeholder for sign-up functionality
        QMessageBox.information(self, 'Login', 'Sign Up functionality to be implemented.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())
