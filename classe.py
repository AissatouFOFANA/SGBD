import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt
import mysql.connector

class ClassListPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste des classes")
        self.setGeometry(100, 100, 400, 300)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Liste des classes")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        container_layout.setAlignment(Qt.AlignCenter)

        try:
            # Connexion à la base de données MySQL
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            # Récupération des noms de classes depuis la base de données
            cursor.execute("SELECT Nom_Classe, Effectif FROM classes")
            classes = cursor.fetchall()

            # Parcourir les classes et ajouter chaque bouton à la mise en page
            for class_info in classes:
                class_name = class_info[0]
                class_button = QPushButton(class_name)
                class_button.setStyleSheet("""
                    QPushButton {
                        margin: 10px;
                        padding: 15px 20px;
                        font-size: 18px;
                        border: none;
                        border-radius: 5px;
                        background-color: #f0f0f0;
                        cursor: pointer;
                    }
                    QPushButton:hover {
                        background-color: #e0e0e0;
                    }
                """)
                class_button.clicked.connect(lambda _, class_name=class_name: self.show_class_info(class_name, connection))
                container_layout.addWidget(class_button)

        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la récupération des classes : {str(e)}")
        finally:
            if connection.is_connected():
                cursor.close()

        layout.addWidget(container_widget)

        return_button = QPushButton("Retour")
        return_button.clicked.connect(self.go_back)
        layout.addWidget(return_button)

        self.setLayout(layout)

    def show_class_info(self, class_name, connection):
        try:
            # Création d'un nouveau curseur pour la base de données
            cursor = connection.cursor()

            # Récupération des informations de la classe depuis la base de données
            cursor.execute("SELECT * FROM classes WHERE Nom_Classe = %s", (class_name,))
            class_info = cursor.fetchone()

            # Demande à l'administrateur de saisir le nouvel effectif
            new_effectif, ok = QInputDialog.getInt(self, "Modifier l'effectif", f"Nouvel effectif pour la classe {class_name}: ", class_info[1], 0, 1000)

            if ok:
                # Mettre à jour l'effectif dans la base de données
                cursor.execute("UPDATE classes SET Effectif = %s WHERE Nom_Classe = %s", (new_effectif, class_name))
                connection.commit()
                QMessageBox.information(self, "Modification réussie", f"L'effectif pour la classe {class_name} a été mis à jour avec succès.")

        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la récupération des informations de la classe : {str(e)}")
        finally:
            # Fermeture du curseur
            cursor.close()

    def go_back(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClassListPage()
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QInputDialog
import mysql.connector

class ClassListPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste des classes")
        self.setGeometry(100, 100, 400, 300)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Liste des classes")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        container_layout.setAlignment(Qt.AlignCenter)

        try:
            # Connexion à la base de données MySQL
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            # Récupération des noms de classes et de leur effectif depuis la base de données
            cursor.execute("SELECT Nom_Classe, Effectif FROM classes")
            classes = cursor.fetchall()

            # Parcourir les classes et ajouter chaque bouton à la mise en page
            for class_info in classes:
                class_name = class_info[0]
                class_button = QPushButton(class_name)
                class_button.setStyleSheet("""
                    QPushButton {
                        margin: 10px;
                        padding: 15px 20px;
                        font-size: 18px;
                        border: none;
                        border-radius: 5px;
                        background-color: #f0f0f0;
                        cursor: pointer;
                    }
                    QPushButton:hover {
                        background-color: #e0e0e0;
                    }
                """)
                class_button.clicked.connect(lambda _, class_name=class_name: self.show_class_info(class_name, connection))
                container_layout.addWidget(class_button)

        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la récupération des classes : {str(e)}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

        layout.addWidget(container_widget)

        return_button = QPushButton("Retour")
        return_button.clicked.connect(self.go_back)
        layout.addWidget(return_button)

        self.setLayout(layout)

    def show_class_info(self, class_name, connection):
        try:
            # Création d'un nouveau curseur pour la base de données
            cursor = connection.cursor()

            # Récupération de l'effectif de la classe depuis la base de données
            cursor.execute("SELECT Effectif FROM classes WHERE Nom_Classe = %s", (class_name,))
            current_effectif = cursor.fetchone()[0]

            # Demande à l'utilisateur de saisir le nouvel effectif
            new_effectif, ok = QInputDialog.getInt(self, "Modifier l'effectif", f"Nouvel effectif pour la classe {class_name}:", current_effectif, 0, 1000)

            if ok:
                # Mise à jour de l'effectif dans la base de données
                cursor.execute("UPDATE classes SET Effectif = %s WHERE Nom_Classe = %s", (new_effectif, class_name))
                connection.commit()
                QMessageBox.information(self, "Modification réussie", f"L'effectif pour la classe {class_name} a été mis à jour avec succès.")

        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la récupération des informations de la classe : {str(e)}")
        finally:
            if 'cursor' in locals():
                cursor.close()

    def go_back(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClassListPage()
    window.show()
    sys.exit(app.exec_())
