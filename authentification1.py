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
        self.profil_combobox.addItems(["Professeur", "Administrateur", "Responsable Pedagogique", "Directeur des Etudes", "Responsable de classe"])
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

        if self.authenticate(login, password, profil):
            self.redirect_to_page(profil)
        else:
            QMessageBox.warning(self, "Erreur de connexion", "Identifiants de connexion incorrects.")

    def authenticate(self, login, password, profil):
        # Implémentez la logique pour vérifier les identifiants de connexion dans la base de données
        # Si les identifiants de connexion sont valides, retournez True, sinon retournez False
        # Vous devez interroger la base de données pour trouver l'utilisateur avec les informations fournies
        # et vérifier si le mot de passe correspond au login et au profil
        # Utilisez une requête SQL pour cela
        # Par exemple, vous pouvez utiliser MySQL, SQLite ou tout autre système de gestion de base de données
        # Pour cet exemple, nous simulons l'authentification en utilisant des identifiants de connexion statiques

        # Simulation de l'authentification (Remplacez ceci par la logique réelle)
        valid_credentials = {
            "admin": {"password": "admin", "profil": "Administrateur"},
            "prof": {"password": "prof", "profil": "Professeur"},
            "resp": {"password": "resp", "profil": "Responsable Pedagogique"},
            "directeur": {"password": "directeur", "profil": "Directeur des Etudes"},
            "resp_classe": {"password": "resp_classe", "profil": "Responsable de classe"}
        }

        if login in valid_credentials:
            return valid_credentials[login]["password"] == password and valid_credentials[login]["profil"] == profil
        else:
            return False

    def redirect_to_page(self, profil):
        if profil == "Administrateur":
            # Redirection vers la page d'administration
            QProcess.startDetached("python", ["admin.py"])
        elif profil == "Professeur":
            # Redirection vers la page du professeur
            QProcess.startDetached("python", ["professeur.py"])
        elif profil == "Responsable Pedagogique":
            # Redirection vers la page du responsable pédagogique
            QProcess.startDetached("python", ["responsable_pedagogique.py"])
        elif profil == "Directeur des Etudes":
            # Redirection vers la page du directeur des études
            QProcess.startDetached("python", ["directeur_des_etudes.py"])
        elif profil == "Responsable de classe":
            # Redirection vers la page du responsable de classe
            QProcess.startDetached("python", ["responsable_de_classe.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthentificationApp()
    window.show()
    sys.exit(app.exec_())
