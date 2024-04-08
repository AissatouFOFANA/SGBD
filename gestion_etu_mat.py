import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QUrl
import mysql.connector
import webbrowser

class ManageStudentsAndSubjectsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion des étudiants et des matières")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Gestion des étudiants et des matières")
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)
        layout.addWidget(title_label)

        class_selection_layout = QHBoxLayout()
        class_label = QLabel("Sélectionner une classe :")
        class_selection_layout.addWidget(class_label)
        self.class_combo_box = QComboBox()
        self.class_combo_box.addItem("Toutes les classes")
        self.load_classes()
        class_selection_layout.addWidget(self.class_combo_box)
        layout.addLayout(class_selection_layout)

        self.students_table = QTableWidget()
        self.students_table.setColumnCount(11)
        self.students_table.setHorizontalHeaderLabels(["ID", "Nom", "Prénom", "Situation Matrimoniale", "Lieu de Naissance", "Date de Naissance", "Mot de passe", "Numéro étudiant", "Sexe", "Classe", "Actions"])
        layout.addWidget(self.students_table)

        self.subjects_table = QTableWidget()
        self.subjects_table.setColumnCount(5)
        self.subjects_table.setHorizontalHeaderLabels(["ID", "Nom", "Coefficient", "Classe", "Actions"])
        layout.addWidget(self.subjects_table)

        buttons_layout = QHBoxLayout()
        add_student_button = QPushButton("Ajouter étudiant")
        add_student_button.clicked.connect(self.add_student)
        buttons_layout.addWidget(add_student_button)
        add_subject_button = QPushButton("Ajouter matière")
        add_subject_button.clicked.connect(self.add_subject)
        buttons_layout.addWidget(add_subject_button)
        back_button = QPushButton("Retour")
        back_button.clicked.connect(self.go_back)
        buttons_layout.addWidget(back_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.class_combo_box.currentIndexChanged.connect(self.load_students_and_subjects)

        self.load_students_and_subjects()

    def load_classes(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            query = "SELECT DISTINCT Nom_Classe FROM Classes"
            cursor.execute(query)
            classes = cursor.fetchall()

            for class_name in classes:
                self.class_combo_box.addItem(class_name[0])

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur :", error)

    def load_students_and_subjects(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            selected_class = self.class_combo_box.currentText()

            # Load students
            query_students = "SELECT Etudiants.*, Classes.Nom_Classe FROM Etudiants INNER JOIN Classes ON Etudiants.ID_Classe = Classes.ID_Classe WHERE :selected_class = '' OR Classes.Nom_Classe = :selected_class"
            cursor.execute(query_students, {"selected_class": selected_class})
            students = cursor.fetchall()
            self.students_table.setRowCount(len(students))
            for i, student in enumerate(students):
                for j, data in enumerate(student):
                    self.students_table.setItem(i, j, QTableWidgetItem(str(data)))

            # Load subjects
            query_subjects = "SELECT Matieres.ID_Matiere, Matieres.Libelle_Matiere, Matieres.coef, Classes.Nom_Classe FROM Matieres INNER JOIN Classes ON Matieres.ID_Classe = Classes.ID_Classe WHERE :selected_class = '' OR Classes.Nom_Classe = :selected_class"
            cursor.execute(query_subjects, {"selected_class": selected_class})
            subjects = cursor.fetchall()
            self.subjects_table.setRowCount(len(subjects))
            for i, subject in enumerate(subjects):
                for j, data in enumerate(subject):
                    self.subjects_table.setItem(i, j, QTableWidgetItem(str(data)))

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur :", error)

    def add_student(self):
        webbrowser.open("compte.py")

    def add_subject(self):
        webbrowser.open("ajouter_matiere.py")

    def go_back(self):
        webbrowser.open("admin.py")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManageStudentsAndSubjectsPage()
    window.show()
    sys.exit(app.exec_())
