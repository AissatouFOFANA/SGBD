import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


class AdminPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Page de l'administrateur")
        self.setGeometry(100, 100, 600, 400)

        # Establish database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gdn"
        )
        self.cursor = self.connection.cursor()

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Administrateur")
        label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        """)
        layout.addWidget(label)

        button_gestion_enseignant = QPushButton("Gestion des enseignants")
        button_gestion_enseignant.setObjectName("gestion_enseignant")
        button_gestion_enseignant.clicked.connect(self.handle_gestion_enseignant)
        layout.addWidget(button_gestion_enseignant)

        button_gestion_etudiants_matieres = QPushButton("Gestion des étudiants et des matières")
        button_gestion_etudiants_matieres.setObjectName("gestion_etudiants_matieres")
        button_gestion_etudiants_matieres.clicked.connect(self.handle_gestion_etudiants_matieres)
        layout.addWidget(button_gestion_etudiants_matieres)

        button_gestion_classes = QPushButton("Gestion des classes")
        button_gestion_classes.setObjectName("gestion_classes")
        button_gestion_classes.clicked.connect(self.handle_gestion_classes)
        layout.addWidget(button_gestion_classes)

        self.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 25px;
                background-color: #F4D03F;
                color: white;
            }
            QPushButton:hover {
                background-color: #E67E22;
            }
            #gestion_enseignant {
                background-color: #3498DB;
            }
            #gestion_enseignant:hover {
                background-color: #2980B9;
            }
            #gestion_etudiants_matieres {
                background-color: #27AE60;
            }
            #gestion_etudiants_matieres:hover {
                background-color: #229954;
            }
            #gestion_classes {
                background-color: #9B59B6;
            }
            #gestion_classes:hover {
                background-color: #8E44AD;
            }
        """)

        self.setLayout(layout)

    def handle_gestion_enseignant(self):
        url = QUrl("gestion_professeurs.py")
        QDesktopServices.openUrl(url)

    def handle_gestion_etudiants_matieres(self):
        url = QUrl("gestion_etu_mat.py")
        QDesktopServices.openUrl(url)

    def handle_gestion_classes(self):
        url = QUrl("gestion_classes.py")
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminPage()
    window.show()
    sys.exit(app.exec_())
