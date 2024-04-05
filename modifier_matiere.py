import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
from PyQt5.QtCore import Qt

class ModifierMatiereApp(QWidget):
    def __init__(self, matiere_id):
        super().__init__()

        self.setWindowTitle("Modifier une matière")
        self.setGeometry(100, 100, 400, 300)

        self.matiere_id = matiere_id

        self.libelle_matiere_input = QLineEdit()
        self.coef_input = QLineEdit()
        self.classe_combobox = QComboBox()
        self.save_button = QPushButton("Enregistrer")
        self.back_button = QPushButton("Retour")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Libellé:"))
        layout.addWidget(self.libelle_matiere_input)

        layout.addWidget(QLabel("Coefficient:"))
        layout.addWidget(self.coef_input)

        layout.addWidget(QLabel("Classe:"))
        layout.addWidget(self.classe_combobox)

        layout.addWidget(self.save_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.save_button.clicked.connect(self.save_changes)
        self.back_button.clicked.connect(self.go_back)

        # Charger les détails de la matière
        self.load_matiere_details()

    def load_matiere_details(self):
        # Ici vous pouvez ajouter le code pour récupérer les détails de la matière à partir de la base de données
        # Pour l'instant, je vais simplement définir des valeurs par défaut
        self.libelle_matiere_input.setText("Nom de la matière")
        self.coef_input.setText("2")

        # Charger les classes depuis la base de données
        # Remplacer cette partie du code par le chargement réel des classes depuis la base de données
        classes = ["Classe 1", "Classe 2", "Classe 3"]
        self.classe_combobox.addItems(classes)

    def save_changes(self):
        # Ici vous pouvez ajouter le code pour enregistrer les modifications dans la base de données
        # Pour l'instant, nous afficherons simplement un message
        QMessageBox.information(self, "Enregistré", "Modifications enregistrées avec succès.")

    def go_back(self):
        # Ici vous pouvez ajouter le code pour revenir à la page précédente ou fermer la fenêtre
        # Pour l'instant, nous fermerons simplement la fenêtre
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModifierMatiereApp("ID_Matiere")
    window.show()
    sys.exit(app.exec_())
