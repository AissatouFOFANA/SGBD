import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QComboBox
from PyQt5.QtCore import QUrl, QCoreApplication
from PyQt5.QtGui import QDesktopServices, QFont
import mysql.connector

class AddClassPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ajouter une classe")
        self.setGeometry(100, 100, 400, 300)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Ajouter une classe")
        label.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        """)
        layout.addWidget(label)

        self.nom_classe_input = QLineEdit()
        self.nom_classe_input.setPlaceholderText("Nom de la classe")
        layout.addWidget(self.nom_classe_input)

        self.niveau_classe_combo = QComboBox()
        self.niveau_classe_combo.addItems(["Niveau1", "Niveau2", "Niveau3", "Niveau4", "Niveau5", "Niveau6", "Niveau7", "Niveau8"])
        layout.addWidget(self.niveau_classe_combo)

        add_button = QPushButton("Ajouter")
        add_button.setStyleSheet("""
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 25px;
            background-color: #F4D03F;
            color: white;
        """)
        add_button.clicked.connect(self.add_class)
        layout.addWidget(add_button)

        back_button = QPushButton("Retour")
        back_button.setStyleSheet("""
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 25px;
            background-color: #9B59B6;
            color: white;
        """)
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def add_class(self):
        nom_classe = self.nom_classe_input.text()
        niveau_classe = self.niveau_classe_combo.currentText()

        if nom_classe:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="gdn"
                )
                cursor = connection.cursor()

                # Vérifier si la classe existe déjà
                query_check = "SELECT * FROM classes WHERE Nom_Classe = %s"
                cursor.execute(query_check, (nom_classe,))
                if cursor.rowcount > 0:
                    print("La classe existe déjà !")
                else:
                    # Insérer la classe
                    query_insert = "INSERT INTO classes (Nom_Classe, Niveau_Classe) VALUES (%s, %s)"
                    cursor.execute(query_insert, (nom_classe, niveau_classe))
                    connection.commit()
                    print("La classe a été ajoutée avec succès !")

                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print("Erreur lors de l'ajout de la classe :", error)
        else:
            print("Veuillez saisir le nom de la classe.")

    def go_back(self):
        # Redirection vers la page de gestion des classes
        url = QUrl("gestion_classes.py")
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddClassPage()
    window.show()
    sys.exit(app.exec_())
