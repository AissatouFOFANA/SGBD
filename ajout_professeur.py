import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QDateEdit
from PyQt5.QtCore import Qt
import mysql.connector
import subprocess

class AddProfessorPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ajouter un professeur")
        self.setGeometry(100, 100, 400, 600)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Ajouter un professeur")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.nom_input = QLineEdit()
        self.setup_line_edit(self.nom_input, "Nom")
        layout.addWidget(self.nom_input)

        self.prenom_input = QLineEdit()
        self.setup_line_edit(self.prenom_input, "Prénom")
        layout.addWidget(self.prenom_input)

        self.situation_matrimoniale_input = QLineEdit()
        self.setup_line_edit(self.situation_matrimoniale_input, "Situation Matrimoniale")
        layout.addWidget(self.situation_matrimoniale_input)

        self.lieu_naissance_input = QLineEdit()
        self.setup_line_edit(self.lieu_naissance_input, "Lieu de Naissance")
        layout.addWidget(self.lieu_naissance_input)

        self.date_naissance_label = QLabel("Date de Naissance")
        layout.addWidget(self.date_naissance_label)

        self.date_naissance_input = QDateEdit(calendarPopup=True)
        layout.addWidget(self.date_naissance_input)

        self.diplome_formation_input = QLineEdit()
        self.setup_line_edit(self.diplome_formation_input, "Diplôme de Formation")
        layout.addWidget(self.diplome_formation_input)

        self.autre_diplome_input = QLineEdit()
        self.setup_line_edit(self.autre_diplome_input, "Autre Diplôme (facultatif)")
        layout.addWidget(self.autre_diplome_input)

        self.matieres_enseignees_input = QLineEdit()
        self.setup_line_edit(self.matieres_enseignees_input, "Matières Enseignées")
        layout.addWidget(self.matieres_enseignees_input)

        self.autre_matiere_input = QLineEdit()
        self.setup_line_edit(self.autre_matiere_input, "Autre Matière (facultatif)")
        layout.addWidget(self.autre_matiere_input)

        self.login_input = QLineEdit()
        self.setup_line_edit(self.login_input, "Login")
        layout.addWidget(self.login_input)

        self.password_input = QLineEdit()
        self.setup_line_edit(self.password_input, "Mot de passe", is_password=True)
        layout.addWidget(self.password_input)

        add_button = QPushButton("Ajouter")
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        add_button.clicked.connect(self.add_professor)
        layout.addWidget(add_button)

        back_button = QPushButton("Retour")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def setup_line_edit(self, line_edit, placeholder, is_password=False):
        line_edit.setPlaceholderText(placeholder)
        if is_password:
            line_edit.setEchoMode(QLineEdit.Password)

    def add_professor(self):
        nom = self.nom_input.text()
        prenom = self.prenom_input.text()
        situation_matrimoniale = self.situation_matrimoniale_input.text()
        lieu_naissance = self.lieu_naissance_input.text()
        date_naissance = self.date_naissance_input.date().toString("yyyy-MM-dd")
        diplome_formation = self.diplome_formation_input.text()
        autre_diplome = self.autre_diplome_input.text()
        matieres_enseignees = self.matieres_enseignees_input.text()
        autre_matiere = self.autre_matiere_input.text()
        login = self.login_input.text()
        password = self.password_input.text()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            query = "INSERT INTO professeurs (Nom, Prenom, Situation_Matrimoniale, Lieu_Naissance, Date_Naissance, Diplome_Formation, Autre_Diplome, Matieres_Enseignees, Autre_Matiere, Login, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nom, prenom, situation_matrimoniale, lieu_naissance, date_naissance, diplome_formation, autre_diplome, matieres_enseignees, autre_matiere, login, password))
            connection.commit()
            print("Le professeur a été ajouté avec succès !")

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur lors de l'ajout du professeur :", error)

    def go_back(self):
        subprocess.Popen(["python", "admin.py"])
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddProfessorPage()
    window.show()
    sys.exit(app.exec_())
