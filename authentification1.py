import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox
from PyQt5.QtCore import QProcess
import mysql.connector

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
        self.profil_combobox.addItems(["Administrateur", "Responsable Pedagogique", "Directeur des Etudes", "Responsable de classe", "Chef de Departement"])
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

        with open("authentification1.css", "r") as f:
            self.setStyleSheet(f.read())

    def login(self):
        login = self.login_input.text()
        password = self.password_input.text()
        profil = self.profil_combobox.currentText()

        if self.authenticate(login, password, profil):
            self.redirect_to_page(profil)
        else:
            QMessageBox.warning(self, "Erreur de connexion", "login ou mot de passe incorrecte.")

    def authenticate(self, login, password, profil):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = db.cursor()

            # Sélectionner la table appropriée en fonction du profil
            if profil == "Administrateur":
                table = "administrateurs"
            elif profil == "Responsable Pedagogique":
                table = "responsables_pedagogiques"
            elif profil == "Directeur des Etudes":
                table = "directeuretudes"
            elif profil == "Responsable de classe":
                table = "responsables_classe"
            elif profil == "Chef de Departement":
                table = "chefdepartement"
            else:
                raise ValueError("Profil non valide")

            # Exécuter une requête SQL pour sélectionner les informations d'identification correspondantes
            query = f"SELECT * FROM {table} WHERE login = %s"
            cursor.execute(query, (login,))
            result = cursor.fetchone()

            # Vérifier si les identifiants de connexion correspondent
            if result and result[1] == password:
                return True
            else:
                return False

        except mysql.connector.Error as err:
            print(f"Erreur MySQL: {err}")
            return False

        finally:
            # Fermer la connexion à la base de données
            if db:
                db.close()

    def redirect_to_page(self, profil):
        if profil == "Administrateur":
            # Redirection vers la page d'administration
            QProcess.startDetached("python", ["admin.py"])
        elif profil == "Responsable Pedagogique":
            # Redirection vers la page du responsable pédagogique
            QProcess.startDetached("python", ["res_peda.py"])
        elif profil == "Directeur des Etudes":
            # Redirection vers la page du directeur des études
            QProcess.startDetached("python", ["directeur.py"])
        elif profil == "Responsable de classe":
            # Redirection vers la page du responsable de classe
            QProcess.startDetached("python", ["respclasse.py"])
        elif profil == "Chef de Departement":
            # Redirection vers la page du chef de departement
            QProcess.startDetached("python", ["chefdepartement.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthentificationApp()
    window.show()
    sys.exit(app.exec_())