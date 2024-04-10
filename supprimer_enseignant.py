from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import mysql.connector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Définir la fenêtre principale
        self.setWindowTitle("Supprimer un enseignant")
        self.setGeometry(100, 100, 280, 170)

        # Créer un widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Créer un layout principal
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Créer un label pour l'identifiant de l'enseignant
        self.label_id = QLabel("Identifiant de l'enseignant :")
        self.main_layout.addWidget(self.label_id)

        # Créer un champ de saisie pour l'identifiant de l'enseignant
        self.input_id = QLineEdit()
        self.main_layout.addWidget(self.input_id)

        # Créer un bouton pour supprimer l'enseignant
        self.button_supprimer = QPushButton("Supprimer")
        self.button_supprimer.clicked.connect(self.supprimer_enseignant)
        self.main_layout.addWidget(self.button_supprimer)

    def supprimer_enseignant(self):
        # Récupérer l'identifiant de l'enseignant
        enseignant_id = self.input_id.text()

        # Vérifier si l'identifiant est vide
        if not enseignant_id:
            QMessageBox.warning(self, "Erreur", "L'identifiant de l'enseignant est vide.")
            return

        # Se connecter à la base de données
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="passer",
                database="gdn",
            )
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erreur", f"Erreur de connexion à la base de données : {e}")
            return

        # Supprimer l'enseignant de la base de données
        try:
            cursor = conn.cursor()
            cursor.execute("START TRANSACTION")
            cursor.execute("DELETE FROM enseignant WHERE id = %s", (enseignant_id,))
            conn.commit()
            QMessageBox.information(self, "Succès", "Enseignant supprimé avec succès.")
        except mysql.connector.Error as e:
            cursor.execute("ROLLBACK")
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la suppression de l'enseignant : {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
