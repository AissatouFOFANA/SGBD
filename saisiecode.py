import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class RecuperationComptePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Récupération de compte")
        self.setGeometry(100, 100, 400, 200)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Récupération de compte")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        code_label = QLabel("Code de récupération :")
        self.code_input = QLineEdit()
        layout.addWidget(code_label)
        layout.addWidget(self.code_input)

        validate_button = QPushButton("Valider")
        validate_button.clicked.connect(self.validate_code)
        layout.addWidget(validate_button)

        self.setLayout(layout)

    def validate_code(self):
        code_saisi = self.code_input.text()

        # Récupérer le code envoyé depuis votre système de stockage (base de données, fichier, etc.)
        code_envoye = "123456"  # Remplacez cela par le code envoyé réel

        # Vérifier si le code saisi est un nombre
        if code_saisi.isdigit():
            # Comparer le code saisi avec le code envoyé
            if int(code_saisi) == int(code_envoye):
                # Les codes correspondent, afficher un message de succès
                QMessageBox.information(self, "Succès", "Le code est correct. Redirection vers la page de réinitialisation.")
                # Rediriger l'utilisateur vers la page de réinitialisation
                # (Vous devez implémenter la page de réinitialisation dans une nouvelle classe QWidget)
                # self.redirect_to_reset_page() 
            else:
                # Les codes ne correspondent pas, afficher un message d'erreur
                QMessageBox.warning(self, "Erreur", "Le code saisi est incorrect.")
        else:
            # Le code saisi n'est pas un nombre, afficher un message d'erreur
            QMessageBox.warning(self, "Erreur", "Veuillez saisir un code numérique.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecuperationComptePage()
    window.show()
    sys.exit(app.exec_())
