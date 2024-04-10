import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QDialog, QDialogButtonBox, QComboBox, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import mysql.connector

class ModifierProfesseurDialog(QDialog):
    def __init__(self, professeur_id):
        super().__init__()

        self.professeur_id = professeur_id

        self.setWindowTitle("Modifier un professeur")
        self.layout = QVBoxLayout()

        self.initUI()

        self.setLayout(self.layout)

    def initUI(self):
        self.form_layout = QFormLayout()

        self.nom_input = QLineEdit()
        self.form_layout.addRow("Nom:", self.nom_input)

        self.prenom_input = QLineEdit()
        self.form_layout.addRow("Prénom:", self.prenom_input)

        self.situation_matrimoniale_input = QComboBox()
        self.situation_matrimoniale_input.addItems(["Célibataire", "Marié(e)", "Veuf(ve)"])
        self.form_layout.addRow("Situation Matrimoniale:", self.situation_matrimoniale_input)

        self.lieu_naissance_input = QLineEdit()
        self.form_layout.addRow("Lieu de Naissance:", self.lieu_naissance_input)

        self.date_naissance_input = QLineEdit()
        self.form_layout.addRow("Date de Naissance:", self.date_naissance_input)

        self.diplome_formation_input = QLineEdit()
        self.form_layout.addRow("Diplôme de Formation:", self.diplome_formation_input)

        self.autre_diplome_input = QLineEdit()
        self.form_layout.addRow("Autre Diplôme:", self.autre_diplome_input)

        self.matieres_enseignees_input = QLineEdit()
        self.form_layout.addRow("Matières Enseignées:", self.matieres_enseignees_input)

        self.autre_matiere_input = QLineEdit()
        self.form_layout.addRow("Autre Matière:", self.autre_matiere_input)

        self.login_input = QLineEdit()
        self.form_layout.addRow("Login:", self.login_input)

        self.passwd_input = QLineEdit()
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.form_layout.addRow("Mot de passe:", self.passwd_input)

        self.submit_button = QPushButton("Enregistrer")
        self.submit_button.clicked.connect(self.update_professeur)
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.submit_button)

    def update_professeur(self):
        nom = self.nom_input.text()
        prenom = self.prenom_input.text()
        situation_matrimoniale = self.situation_matrimoniale_input.currentText()
        lieu_naissance = self.lieu_naissance_input.text()
        date_naissance = self.date_naissance_input.text()
        diplome_formation = self.diplome_formation_input.text()
        autre_diplome = self.autre_diplome_input.text()
        matieres_enseignees = self.matieres_enseignees_input.text()
        autre_matiere = self.autre_matiere_input.text()
        login = self.login_input.text()
        passwd = self.passwd_input.text()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = db.cursor()

            query = "UPDATE professeurs SET Nom_Professeur = %s, Prenom_Professeur = %s, Situation_Matrimoniale = %s, Lieu_Naissance = %s, Date_Naissance = %s, Diplome_Formation = %s, Autre_Diplome = %s, Matieres_Enseignees = %s, Autre_Matiere = %s, Login_Professeur = %s, Passwd_Professeur = %s WHERE ID_Professeur = %s"
            data = (nom, prenom, situation_matrimoniale, lieu_naissance, date_naissance, diplome_formation, autre_diplome, matieres_enseignees, autre_matiere, login, passwd, self.professeur_id)
            cursor.execute(query, data)
            db.commit()
            db.close()

            QMessageBox.information(self, "Success", "Les informations du professeur ont été mises à jour avec succès.")
            self.accept()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Erreur : {err}")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modifier un professeur")
        self.layout = QVBoxLayout()

        self.initUI()

        self.setLayout(self.layout)

    def initUI(self):
        self.id_label = QLabel("ID du professeur:")
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Entrez l'ID du professeur")

        self.load_button = QPushButton("Charger")
        self.load_button.clicked.connect(self.load_professeur)

        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.id_input)
        self.layout.addWidget(self.load_button)

    def load_professeur(self):
        professeur_id = self.id_input.text()
        if professeur_id:
            dialog = ModifierProfesseurDialog(professeur_id)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "Warning", "Veuillez entrer l'ID du professeur.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
