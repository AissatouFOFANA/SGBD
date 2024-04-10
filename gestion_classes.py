import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QLineEdit
from PyQt5.QtWidgets import QMessageBox, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QUrl, Qt
import mysql.connector
from PyQt5.QtGui import QDesktopServices
import webbrowser

class ManageClassesPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion des classes")
        self.setGeometry(100, 100, 600, 400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Gestion des classes")
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)
        layout.addWidget(title_label)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Rechercher par nom ou niveau")
        search_layout.addWidget(self.search_input)
        search_button = QPushButton("Rechercher")
        search_button.clicked.connect(self.search_classes)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        self.classes_table = QTableWidget()
        self.classes_table.setColumnCount(4)
        self.classes_table.setHorizontalHeaderLabels(["ID", "Nom", "Niveau", "Actions"])
        layout.addWidget(self.classes_table)

        buttons_layout = QHBoxLayout()
        add_class_button = QPushButton("Ajouter classe")
        add_class_button.clicked.connect(self.add_class)
        buttons_layout.addWidget(add_class_button)
        back_button = QPushButton("Retour")
        back_button.clicked.connect(self.go_back)
        buttons_layout.addWidget(back_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.load_classes()

    def load_classes(self):
        self.classes_table.setRowCount(0)

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            search_text = self.search_input.text()

            query = "SELECT * FROM classes WHERE Nom_Classe LIKE %s OR Niveau_Classe LIKE %s"
            cursor.execute(query, (f"%{search_text}%", f"%{search_text}%"))
            classes = cursor.fetchall()

            for row_number, row_data in enumerate(classes):
                self.classes_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.classes_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                # Ajouter les boutons dans la colonne des actions
                modify_button = QPushButton("Modifier")
                delete_button = QPushButton("Supprimer")
                modify_button.clicked.connect(lambda _, id=row_data[0]: self.modify_class(id))
                delete_button.clicked.connect(lambda _, id=row_data[0]: self.delete_class(id))
                buttons_layout = QHBoxLayout()
                buttons_layout.addWidget(modify_button)
                buttons_layout.addWidget(delete_button)
                buttons_layout.setContentsMargins(0, 0, 0, 0)
                buttons_widget = QWidget()
                buttons_widget.setLayout(buttons_layout)
                self.classes_table.setCellWidget(row_number, 3, buttons_widget)

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur :", error)

    def search_classes(self):
        self.load_classes()

    def add_class(self):
        # Redirection vers la page d'ajout de classe
        webbrowser.open("ajout_classe.py")

    def modify_class(self, ID_Classe):
    # Récupérer les informations de la classe
        try:
            conn = self.get_database_connection()
            cursor = conn.cursor()

            query = "SELECT * FROM classes WHERE ID_Classe = :id"
            cursor.execute(query, {"id": ID_Classe})
            classe = cursor.fetchone()

            if not classe:
                raise Exception("Classe introuvable.")

            # Afficher les informations dans des champs de saisie
            self.nom_classe_input.setText(classe["Nom_Classe"])
            self.niveau_scolaire_input.setText(classe["Niveau_Classe"])
            self.effectif_classe_input.setText(str(classe["Effectif"]))

        except Exception as e:
            raise Exception(f"Erreur lors de la récupération des informations de la classe : {e}")

        # Mettre à jour les informations de la classe
        try:
            nom_classe = self.nom_classe_input.text()
            niveau_scolaire = self.niveau_scolaire_input.text()
            effectif = int(self.effectif_classe_input.text())

            # Vérifier la validité de l'effectif
            if not effectif or effectif <= 0:
                raise ValueError("Effectif invalide.")

            query = """
            UPDATE classes 
            SET Nom_Classe = :nom, 
                Niveau_Classe = :niveau, 
                Effectif = :effectif
            WHERE ID_Classe = :id
            """
            cursor.execute(query, {
                "id": ID_Classe,
                "nom": nom_classe,
                "niveau": niveau_scolaire,
                "effectif": effectif,
            })

            conn.commit()

            # Afficher un message de confirmation
            QMessageBox.information(self, "Succès", "Les informations de la classe ont été modifiées avec succès.")

        except ValueError as e:
            QMessageBox.warning(self, "Erreur", str(e))
        except Exception as e:
            raise Exception(f"Erreur lors de la mise à jour des informations de la classe : {e}")

        finally:
            if conn:
                conn.close()





    def delete_class(self, class_id):
    # Confirmation de la suppression
        reply = QMessageBox.question(self, "Confirmation", "Souhaitez-vous vraiment supprimer cette classe ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.No:
            return

        # Vérifier si la classe est liée à des élèves
        try:
            connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="gdn"
                )
            cursor = connection.cursor()
            query = "SELECT COUNT(*) FROM eleves WHERE ID_Classe = :id"
            cursor.execute(query, {"id": ID_Classe})
            nb_eleves = cursor.fetchone()[0]

            if nb_eleves > 0:
                raise Exception("La classe est liée à des élèves et ne peut pas être supprimée.")

        except Exception as e:
            raise Exception(f"Erreur lors de la vérification des élèves de la classe : {e}")

        # Supprimer la classe de la base de données
        try:
            query = "DELETE FROM classes WHERE ID_Classe = :id"
            cursor.execute(query, {"id": ID_Classe})

            conn.commit()

            # Afficher un message de confirmation
            QMessageBox.information(self, "Succès", "La classe a été supprimée avec succès.")

        except Exception as e:
            raise Exception(f"Erreur lors de la suppression de la classe : {e}")

        finally:
            if conn:
                conn.close()


    def go_back(self):
            # Redirection vers la page d'administration
            webbrowser.open("admin.py")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManageClassesPage()
    window.show()
    sys.exit(app.exec_())
