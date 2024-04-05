import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QColor, QPalette
import mysql.connector

class AddSubjectsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ajout des matières")
        self.setGeometry(100, 100, 500, 400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Ajout des matières pour une classe spécifique")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title_label)

        self.class_combo = QComboBox()
        self.class_combo.setFont(QFont("Arial", 12))
        layout.addWidget(self.class_combo)

        self.subjects_layout = QVBoxLayout()
        self.add_subject_fields()
        layout.addLayout(self.subjects_layout)

        add_button = QPushButton("Ajouter")
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #F4D03F;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 25px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #F7DC6F;
            }
        """)
        add_button.clicked.connect(self.add_subjects)
        layout.addWidget(add_button)

        back_button = QPushButton("Retour")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #9B59B6;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 25px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #BB8FCE;
            }
        """)
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def add_subject_fields(self):
        self.subject_fields = []
        subject_layout = QHBoxLayout()
        label = QLabel("Libellé :")
        label.setFont(QFont("Arial", 12))
        subject_layout.addWidget(label)
        self.libelle_input = QLineEdit()
        self.libelle_input.setFont(QFont("Arial", 12))
        subject_layout.addWidget(self.libelle_input)
        label = QLabel("Coefficient :")
        label.setFont(QFont("Arial", 12))
        subject_layout.addWidget(label)
        self.coef_input = QLineEdit()
        self.coef_input.setFont(QFont("Arial", 12))
        subject_layout.addWidget(self.coef_input)
        self.subjects_layout.addLayout(subject_layout)
        self.subject_fields.append((self.libelle_input, self.coef_input))

    def add_subjects(self):
        classe_id = self.class_combo.currentData()
        subjects = [(field[0].text(), field[1].text()) for field in self.subject_fields]

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            existing_subjects = []
            check_query = "SELECT Libelle_Matiere FROM matieres WHERE ID_Classe = %s"
            cursor.execute(check_query, (classe_id,))
            results = cursor.fetchall()
            for result in results:
                existing_subjects.append(result[0])

            insert_query = "INSERT INTO matieres (Libelle_Matiere, coef, ID_Classe) VALUES (%s, %s, %s)"
            added_subjects = 0

            for subject in subjects:
                libelle, coef = subject
                if libelle in existing_subjects:
                    continue

                cursor.execute(insert_query, (libelle, coef, classe_id))
                added_subjects += 1

            if added_subjects > 0:
                print(f"{added_subjects} matière(s) ont été ajoutée(s) avec succès pour la classe sélectionnée.")
            else:
                print("Cette matière existe déjà pour la classe sélectionnée.")

            connection.commit()
            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur lors de l'ajout des matières :", error)

    def go_back(self):
        # Redirection vers la page de gestion des étudiants et des matières
        url = QUrl("gestion_etu_mat.py")
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddSubjectsPage()
    window.show()
    sys.exit(app.exec_())
