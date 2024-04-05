import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
from PyQt5.QtCore import Qt

class InscriptionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inscription")
        self.setGeometry(100, 100, 400, 300)

        self.login_label = QLabel("Login:")
        self.login_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.profil_label = QLabel("Profil:")
        self.profil_combobox = QComboBox()
        self.profil_combobox.addItems(["Etudiant", "Professeur"])
        self.forget_link = QLabel("<a href='recuperation.php'>Mot de passe oublié ?</a>")
        self.inscription_link = QLabel("<a href='authentification1.php'>Se connecter</a>")
        self.register_button = QPushButton("S'inscrire")

        self.error_label = QLabel()
        self.success_label = QLabel()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QVBoxLayout()
        form_layout.addWidget(self.login_label)
        form_layout.addWidget(self.login_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.confirm_password_label)
        form_layout.addWidget(self.confirm_password_input)
        form_layout.addWidget(self.profil_label)
        form_layout.addWidget(self.profil_combobox)
        form_layout.addWidget(self.forget_link)
        form_layout.addWidget(self.inscription_link)
        form_layout.addWidget(self.register_button)

        layout.addLayout(form_layout)
        layout.addWidget(self.error_label)
        layout.addWidget(self.success_label)

        self.setLayout(layout)

        self.register_button.clicked.connect(self.register)

    def register(self):
        login = self.login_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        profil = self.profil_combobox.currentText()

        if password != confirm_password:
            self.show_error("Les mots de passe ne correspondent pas.")
            return

        # Redirection en fonction du profil (non implémenté)

        self.show_success("Inscription validée.")

    def show_error(self, message):
        self.error_label.setText(f"<font color='red'>{message}</font>")

    def show_success(self, message):
        self.success_label.setText(f"<font color='green'>{message}</font>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InscriptionApp()
    window.show()
    sys.exit(app.exec_())
