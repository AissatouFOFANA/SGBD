import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
import mysql.connector


class PageSelectionClasse(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste des classes")
        self.setGeometry(100, 100, 600, 400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        titre_label = QLabel("Choisissez la classe que vous souhaitez")
        titre_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)
        layout.addWidget(titre_label)

        layout_recherche = QHBoxLayout()
        label_recherche = QLabel("Rechercher une classe :")
        layout_recherche.addWidget(label_recherche)
        self.champ_recherche = QLineEdit()
        layout_recherche.addWidget(self.champ_recherche)
        bouton_recherche = QPushButton("Rechercher")
        bouton_recherche.clicked.connect(self.rechercher_classes)
        layout_recherche.addWidget(bouton_recherche)
        layout.addLayout(layout_recherche)

        self.layout_classes = QVBoxLayout()
        layout.addLayout(self.layout_classes)

        bouton_retour = QPushButton("Retour")
        bouton_retour.clicked.connect(self.retour)
        layout.addWidget(bouton_retour)

        self.setLayout(layout)

        self.charger_classes()

    def charger_classes(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            query = "SELECT * FROM classes"
            cursor.execute(query)
            classes = cursor.fetchall()

            for classe in classes:
                nom_classe = classe[1]
                bouton_classe = QPushButton(nom_classe)
                bouton_classe.setStyleSheet("""
                    QPushButton {
                        display: block;
                        width: 200px;
                        padding: 10px;
                        margin: 10px;
                        text-align: center;
                        background-color: #f0f0f0;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        text-decoration: none;
                        color: #333;
                        font-weight: bold;
                    }
                """)
                bouton_classe.clicked.connect(lambda _, nom=nom_classe: self.redirection_gestion(nom))
                self.layout_classes.addWidget(bouton_classe)

            cursor.close()
            connection.close()
        except mysql.connector.Error as erreur:
            print("Erreur :", erreur)

    def rechercher_classes(self):
        texte_recherche = self.champ_recherche.text()
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            query = "SELECT * FROM classes WHERE Nom_Classe LIKE %s"
            cursor.execute(query, ('%' + texte_recherche + '%',))
            classes = cursor.fetchall()

            self.layout_classes.deleteLater()
            self.layout_classes = QVBoxLayout()
            self.layout().insertLayout(1, self.layout_classes)

            for classe in classes:
                nom_classe = classe[1]
                bouton_classe = QPushButton(nom_classe)
                bouton_classe.setStyleSheet("""
                    QPushButton {
                        display: block;
                        width: 200px;
                        padding: 10px;
                        margin: 10px;
                        text-align: center;
                        background-color: #f0f0f0;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        text-decoration: none;
                        color: #333;
                        font-weight: bold;
                    }
                """)
                bouton_classe.clicked.connect(lambda _, nom=nom_classe: self.redirection_gestion(nom))
                self.layout_classes.addWidget(bouton_classe)

            cursor.close()
            connection.close()
        except mysql.connector.Error as erreur:
            print("Erreur :", erreur)

    def redirection_gestion(self, nom_classe):
        print(f"Redirection vers la gestion de la classe : {nom_classe}")

    def retour(self):
        print("Retour à la page précédente")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = PageSelectionClasse()
    fenetre.show()
    sys.exit(app.exec_())
