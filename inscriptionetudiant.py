import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import Qt
import mysql.connector

class InscriptionEtudiantPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inscription Etudiants")
        self.setGeometry(100, 100, 400, 400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Titre
        title_label = QLabel("Formulaire d'inscription étudiant")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Formulaire
        form_layout = QVBoxLayout()

        nom_label = QLabel("Nom :")
        self.nom_input = QLineEdit()
        form_layout.addWidget(nom_label)
        form_layout.addWidget(self.nom_input)

        prenom_label = QLabel("Prénom :")
        self.prenom_input = QLineEdit()
        form_layout.addWidget(prenom_label)
        form_layout.addWidget(self.prenom_input)

        situation_matrimoniale_label = QLabel("Situation matrimoniale :")
        self.situation_matrimoniale_combo = QComboBox()
        self.situation_matrimoniale_combo.addItems(["Marié(e)", "Célibataire"])
        form_layout.addWidget(situation_matrimoniale_label)
        form_layout.addWidget(self.situation_matrimoniale_combo)

        lieu_naissance_label = QLabel("Lieu de naissance :")
        self.lieu_naissance_input = QLineEdit()
        form_layout.addWidget(lieu_naissance_label)
        form_layout.addWidget(self.lieu_naissance_input)

        date_naissance_label = QLabel("Date de naissance :")
        self.date_naissance_input = QLineEdit()
        form_layout.addWidget(date_naissance_label)
        form_layout.addWidget(self.date_naissance_input)

        num_etudiant_label = QLabel("Numéro d'étudiant :")
        self.num_etudiant_input = QLineEdit()
        form_layout.addWidget(num_etudiant_label)
        form_layout.addWidget(self.num_etudiant_input)

        sexe_label = QLabel("Sexe :")
        self.sexe_combo = QComboBox()
        self.sexe_combo.addItems(["Homme", "Femme"])
        form_layout.addWidget(sexe_label)
        form_layout.addWidget(self.sexe_combo)

        login_label = QLabel("Login :")
        self.login_input = QLineEdit()
        form_layout.addWidget(login_label)
        form_layout.addWidget(self.login_input)

        password_label = QLabel("Mot de passe :")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)

        layout.addLayout(form_layout)

        # Bouton Soumettre
        submit_button = QPushButton("S'inscrire")
        submit_button.clicked.connect(self.register_student)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def register_student(self):
        # Récupérer les données du formulaire
        nom = self.nom_input.text()
        prenom = self.prenom_input.text()
        situation_matrimoniale = self.situation_matrimoniale_combo.currentText()
        lieu_naissance = self.lieu_naissance_input.text()
        date_naissance = self.date_naissance_input.text()
        num_etudiant = self.num_etudiant_input.text()
        sexe = self.sexe_combo.currentText()
        login = self.login_input.text()
        password = self.password_input.text()

        # Connexion à la base de données
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            # Préparer la requête d'insertion
            query = "INSERT INTO Etudiants (Nom_Etudiant, Prenom_Etudiant, Situation_Matrimoniale, Lieu_Naissance, Date_Naissance, Login_Etudiant, Passwd_Etudiant, Num_Etu_Etudiant, Sexe_Etudiant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (nom, prenom, situation_matrimoniale, lieu_naissance, date_naissance, login, password, num_etudiant, sexe)
            cursor.execute(query, values)

            # Commit et fermer la connexion
            connection.commit()
            cursor.close()
            connection.close()

            print("Enregistrement réussi.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement :", error)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InscriptionEtudiantPage()
    window.show()
    sys.exit(app.exec_())
