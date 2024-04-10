import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QUrl
import mysql.connector
from PyQt5.QtGui import QDesktopServices

class GestionProfesseursPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion des professeurs")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Titre
        title_label = QLabel("Gestion des professeurs")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Formulaire de recherche
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Rechercher par nom ou prénom")
        search_layout.addWidget(self.search_input)
        search_button = QPushButton("Rechercher")
        search_button.clicked.connect(self.search_professeurs)
        search_layout.addWidget(search_button)
        main_layout.addLayout(search_layout)

        # Tableau des professeurs
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(13)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nom", "Prénom", "Situation Matrimoniale", "Lieu de Naissance", 
                                                     "Date de Naissance", "Diplôme de Formation", "Autre Diplôme", 
                                                     "Matières Enseignées", "Autre Matière", "Login", "Mot de passe", "Actions"])
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.table_widget)

        # Boutons d'actions
        actions_layout = QHBoxLayout()
        ajouter_button = QPushButton("Ajouter professeur")
        ajouter_button.clicked.connect(self.ajouter_professeur)
        actions_layout.addWidget(ajouter_button)
        retour_button = QPushButton("Retour")
        retour_button.clicked.connect(self.go_back)
        actions_layout.addWidget(retour_button)
        main_layout.addLayout(actions_layout)

        self.setLayout(main_layout)

        # Charger les professeurs au démarrage
        self.load_professeurs()

    def load_professeurs(self):
        # Connexion à la base de données
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            # Récupérer la liste des professeurs
            query = "SELECT * FROM professeurs"
            cursor.execute(query)
            professeurs = cursor.fetchall()

            # Afficher les professeurs dans le tableau
            self.table_widget.setRowCount(len(professeurs))
            for row, professeur in enumerate(professeurs):
                for col, data in enumerate(professeur):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(row, col, item)

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur :", error)

    def search_professeurs(self):
        # Connexion à la base de données et recherche des professeurs
        search_text = self.search_input.text()
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            query = "SELECT * FROM professeurs WHERE Nom_Professeur LIKE %s OR Prenom_Professeur LIKE %s"
            cursor.execute(query, ('%' + search_text + '%', '%' + search_text + '%'))
            professeurs = cursor.fetchall()

            # Afficher les résultats dans le tableau
            self.table_widget.setRowCount(len(professeurs))
            for row, professeur in enumerate(professeurs):
                for col, data in enumerate(professeur):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(row, col, item)

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur :", error)

    def ajouter_professeur(self):
        # Redirection vers la page d'ajout de professeur
       url = QUrl("ajout_professeur.py")
       QDesktopServices.openUrl(url)

    def go_back(self):
        # Redirection vers la page précédente
       url = QUrl("admin.py")
       QDesktopServices.openUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestionProfesseursPage()
    window.show()
    sys.exit(app.exec_())
