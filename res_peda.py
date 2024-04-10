import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import pymysql

class CahierTexteViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cahier Texte Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Créez une connexion à la base de données MySQL
        db = pymysql.connect(host='localhost', user='votre_utilisateur', password='votre_mot_de_passe', database='votre_base_de_donnees')
        cursor = db.cursor()

        # Exécutez une requête SQL pour récupérer les données de la table cahiertexte
        cursor.execute("SELECT libelle, date_cours, programme FROM cahiertexte")
        result = cursor.fetchall()

        # Créez un QTableWidget pour afficher les données
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(50, 50, 700, 500)

        # Remplissez la table avec les données de la table cahiertexte
        for row_number, row_data in enumerate(result):
            self.table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_widget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CahierTexteViewer()
    window.show()
    sys.exit(app.exec_())
