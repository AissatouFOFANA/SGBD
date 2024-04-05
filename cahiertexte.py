import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QTextEdit, QPushButton, QMessageBox, QCalendarWidget, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
import mysql.connector

class CahierJournalier(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cahier Journalier")
        self.setGeometry(100, 100, 800, 600)

        self.selected_date = QDate.currentDate()  # Ajout de l'attribut pour stocker la date sélectionnée

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Création du calendrier
        self.calendar_label = QLabel("Calendrier")
        self.calendar_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.calendar_label, 0, 0, 1, 3)

        self.calendar = QCalendarWidget()
        self.calendar.setSelectedDate(self.selected_date)  # Sélectionner la date initiale
        self.calendar.clicked.connect(self.select_date)  # Connecter le signal de clic à la méthode select_date
        layout.addWidget(self.calendar, 1, 0, 1, 3)

        # Création de la zone de saisie pour le libellé du cours et le programme journalier
        self.label_course = QLabel("Libellé du cours :")
        layout.addWidget(self.label_course, 3, 0)

        self.course_edit = QTextEdit()
        layout.addWidget(self.course_edit, 3, 1, 1, 2)

        self.label_program = QLabel("Programme journalier :")
        layout.addWidget(self.label_program, 4, 0)

        self.program_edit = QTextEdit()
        layout.addWidget(self.program_edit, 4, 1, 1, 2)

        # Boutons pour ajouter et afficher le contenu du jour
        self.add_button = QPushButton("Ajouter")
        self.add_button.clicked.connect(self.add_content)
        layout.addWidget(self.add_button, 5, 0)

        self.show_button = QPushButton("Afficher")
        self.show_button.clicked.connect(self.show_content)
        layout.addWidget(self.show_button, 5, 1)

        self.setLayout(layout)

    def select_date(self, date):
        self.selected_date = date  # Mettre à jour la date sélectionnée

    def add_content(self):
        course_text = self.course_edit.toPlainText()
        program_text = self.program_edit.toPlainText()

        if course_text:
            try:
                # Connexion à la base de données MySQL
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="gdn"
                )
                cursor = connection.cursor()

                # Insertion des informations dans la table cahiertexte
                insert_query = "INSERT INTO cahiertexte (libelle, date_cours, programme) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (course_text, self.selected_date.toString(Qt.ISODate), program_text))
                connection.commit()

                QMessageBox.information(self, "Ajout réussi", "Contenu ajouté avec succès pour le jour sélectionné.")
                self.course_edit.clear()
                self.program_edit.clear()
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"Erreur lors de l'ajout du contenu : {str(e)}")
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez remplir le champ 'Libellé du cours'.")

    def show_content(self):
        try:
            # Connexion à la base de données MySQL
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            # Récupération du contenu de la table cahiertexte
            select_query = "SELECT libelle, date_cours, programme FROM cahiertexte"
            cursor.execute(select_query)
            rows = cursor.fetchall()

            # Affichage des données dans une boîte de dialogue
            dialog = QDialog(self)
            dialog.setWindowTitle("Contenu de la table cahiertexte")
            dialog_layout = QVBoxLayout()

            table = QTableWidget()
            table.setRowCount(len(rows))
            table.setColumnCount(3)
            table.setHorizontalHeaderLabels(["Libellé du cours", "Date du cours", "Programme journalier"])

            for i, row in enumerate(rows):
                for j, item in enumerate(row):
                    table.setItem(i, j, QTableWidgetItem(str(item)))

            dialog_layout.addWidget(table)
            dialog.setLayout(dialog_layout)
            dialog.exec_()
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de l'affichage du contenu : {str(e)}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CahierJournalier()
    window.show()
    sys.exit(app.exec_())
