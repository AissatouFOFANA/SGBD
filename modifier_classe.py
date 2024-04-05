import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import Qt
import mysql.connector

class ModifierClassePage(QWidget):
    def __init__(self, classe_id):
        super().__init__()

        self.setWindowTitle("Modifier une classe")
        self.setGeometry(100, 100, 400, 300)

        self.classe_id = classe_id

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Titre
        title_label = QLabel("Modifier une classe")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Connexion à la base de données
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            # Récupérer les détails de la classe
            query = "SELECT * FROM classes WHERE ID_Classe = %s"
            cursor.execute(query, (self.classe_id,))
            classe = cursor.fetchone()

            if not classe:
                print("Classe introuvable.")
                return

            # Formulaire de modification
            form_layout = QVBoxLayout()

            nom_classe_label = QLabel("Nom de la classe :")
            self.nom_classe_input = QLineEdit()
            self.nom_classe_input.setText(classe[1])
            form_layout.addWidget(nom_classe_label)
            form_layout.addWidget(self.nom_classe_input)

            niveau_classe_label = QLabel("Niveau de la classe :")
            self.niveau_classe_combo = QComboBox()
            niveaux = ["Niveau1", "Niveau2", "Niveau3", "Niveau4", "Niveau5", "Niveau6", "Niveau7", "Niveau8"]
            self.niveau_classe_combo.addItems(niveaux)
            self.niveau_classe_combo.setCurrentText(classe[2])
            form_layout.addWidget(niveau_classe_label)
            form_layout.addWidget(self.niveau_classe_combo)

            layout.addLayout(form_layout)

            # Bouton Enregistrer
            save_button = QPushButton("Enregistrer")
            save_button.clicked.connect(self.update_class)
            layout.addWidget(save_button)

            self.setLayout(layout)

            # Fermer la connexion
            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Erreur lors de la connexion à la base de données :", error)

    def update_class(self):
        try:
            # Connexion à la base de données
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            # Récupérer les nouvelles valeurs du formulaire
            nom_classe = self.nom_classe_input.text()
            niveau_classe = self.niveau_classe_combo.currentText()

            # Mettre à jour les informations de la classe dans la base de données
            query = "UPDATE classes SET Nom_Classe = %s, Niveau_Classe = %s WHERE ID_Classe = %s"
            values = (nom_classe, niveau_classe, self.classe_id)
            cursor.execute(query, values)

            # Commit et fermer la connexion
            connection.commit()
            cursor.close()
            connection.close()

            print("Les informations de la classe ont été mises à jour avec succès.")
        except mysql.connector.Error as error:
            print("Erreur lors de la mise à jour de la classe :", error)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    classe_id = 1  # Remplacez 1 par l'ID de la classe que vous souhaitez modifier
    window = ModifierClassePage(classe_id)
    window.show()
    sys.exit(app.exec_())
