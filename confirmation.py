import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont

class ConfirmationPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Confirmation")
        self.setGeometry(100, 100, 400, 300)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Confirmation")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title_label)

        message_label = QLabel("Un email de récupération a été envoyé à votre adresse email.")
        layout.addWidget(message_label)

        return_button = QPushButton("Retour")
        return_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
                background-color: #3498db;
                color: white;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        layout.addWidget(return_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfirmationPage()
    window.show()
    sys.exit(app.exec_())
