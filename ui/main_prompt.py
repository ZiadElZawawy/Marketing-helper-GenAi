import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QHBoxLayout

class SimpleTextGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create layout containers
        self.layout = QHBoxLayout(self)  # Main layout
        self.leftLayout = QVBoxLayout()  # Layout for input
        self.rightLayout = QVBoxLayout()  # Layout for display

        # Create widgets
        self.textEntry = QLineEdit(self)
        self.sendButton = QPushButton('Send', self)
        self.textLabel = QLabel('Entered text will appear here.', self)

        # Set up layouts
        self.leftLayout.addWidget(self.textEntry)
        self.leftLayout.addWidget(self.sendButton)

        self.rightLayout.addWidget(self.textLabel)

        self.layout.addLayout(self.leftLayout)
        self.layout.addLayout(self.rightLayout)

        # Set up button click connection
        self.sendButton.clicked.connect(self.displayText)

        # Window settings
        self.setWindowTitle('Simple Text GUI with PyQt')
        self.setGeometry(300, 300, 400, 200)  # x, y, width, height

    def displayText(self):
        entered_text = self.textEntry.text()
        self.textLabel.setText(entered_text)
        self.textEntry.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleTextGUI()
    ex.show()
    sys.exit(app.exec_())
