import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox
from PyQt5.QtCore import QProcess

class AuthentificationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authentification")
        self.setGeometry(100, 100, 400, 300)

        self.login_label = QLabel("Login:")
        self.login_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.profil_label = QLabel("Profil:")
        self.profil_combobox = QComboBox()
        self.profil_combobox.addItems(["Etudiant", "Professeur", "Administrateur", "Responsable Pedagogique", "Directeur des Etudes", "Responsable de classe"])
        self.forget_link = QLabel("<a href='#'>Mot de passe oublié ?</a>")
        self.inscription_link = QLabel("<a href='inscription1.py'>S'inscrire</a>")
        self.login_button = QPushButton("Se connecter")

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
        form_layout.addWidget(self.profil_label)
        form_layout.addWidget(self.profil_combobox)
        form_layout.addWidget(self.forget_link)
        form_layout.addWidget(self.inscription_link)
        form_layout.addWidget(self.login_button)

        layout.addLayout(form_layout)
        layout.addWidget(self.error_label)
        layout.addWidget(self.success_label)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)

    def login(self):
        login = self.login_input.text()
        password = self.password_input.text()
        profil = self.profil_combobox.currentText()

        # Ajoutez ici la logique pour vérifier les identifiants de connexion
        # Pour l'instant, nous afficherons simplement un message de connexion réussie
        # QMessageBox.information(self, "Connexion réussie", f"Connexion réussie en tant que {profil}.")

        # Redirection vers différentes pages en fonction du profil
        if profil == "Professeur":
            # Spécifiez le chemin absolu vers pageprof1.py
            QProcess.startDetached("python", ["pageprof1.py"])
        elif profil == "Etudiant":
            # Spécifiez le chemin absolu vers pageetudiant1.py
            QProcess.startDetached("python", ["etudiant.py"])
        elif profil == "Administrateur":
            # Spécifiez le chemin absolu vers pageadmin1.py
            QProcess.startDetached("python", ["admin.py"])
        elif profil == "Responsable Pedagogique":
            # Spécifiez le chemin absolu vers pageresp1.py
            QProcess.startDetached("python", ["pageresp1.py"])
        elif profil == "Directeur des Etudes":
            # Spécifiez le chemin absolu vers pagedir1.py
            QProcess.startDetached("python", ["pagedir1.py"])

        # Fermer la fenêtre d'authentification
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthentificationApp()
    window.show()
    sys.exit(app.exec_())
