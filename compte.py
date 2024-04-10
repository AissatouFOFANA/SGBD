import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QComboBox, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, QInputDialog
from PyQt5.QtCore import Qt
import mysql.connector

class ComptePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion des comptes")
        self.setGeometry(100, 100, 600, 400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Gestion des comptes")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Formulaire de création de compte
        create_layout = QVBoxLayout()
        create_layout.addWidget(QLabel("Créer un compte"))

        self.login_input = QLineEdit()
        self.setup_line_edit(self.login_input, "Login")
        create_layout.addWidget(self.login_input)

        self.password_input = QLineEdit()
        self.setup_line_edit(self.password_input, "Mot de passe", is_password=True)
        create_layout.addWidget(self.password_input)

        self.role_combobox = QComboBox()
        self.role_combobox.addItems(["Etudiant", "Responsable pédagogique", "Responsable de classe", "Chef de département", "Directeur des études"])
        create_layout.addWidget(self.role_combobox)

        create_button = QPushButton("Créer le compte")
        create_button.clicked.connect(self.create_account)
        create_layout.addWidget(create_button)

        layout.addLayout(create_layout)

        # Barre de recherche
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Rechercher")
        self.search_input.textChanged.connect(self.filter_accounts)
        layout.addWidget(self.search_input)

        # Tableau pour afficher les comptes existants
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)  # Ajout de colonnes pour Modifier et Supprimer
        self.table_widget.setHorizontalHeaderLabels(["ID", "Login", "Rôle", "Modifier", "Supprimer"])

        # Redimensionner la largeur de la colonne de l'action
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table_widget)

        # Bouton pour rafraîchir la liste des comptes
        refresh_button = QPushButton("Actualiser")
        refresh_button.clicked.connect(self.refresh_accounts)
        layout.addWidget(refresh_button)

        self.setLayout(layout)

        # Actualisation de la liste des comptes lors du lancement
        self.refresh_accounts()

    def setup_line_edit(self, line_edit, placeholder, is_password=False):
        line_edit.setPlaceholderText(placeholder)
        if is_password:
            line_edit.setEchoMode(QLineEdit.Password)

    def create_account(self):
        login = self.login_input.text()
        password = self.password_input.text()
        role = self.role_combobox.currentText()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            query = "INSERT INTO compte (login, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (login, password, role))
            connection.commit()
            QMessageBox.information(self, "Succès", "Le compte a été créé avec succès !")

            cursor.close()
            connection.close()

            # Rafraîchir la liste des comptes après la création
            self.refresh_accounts()

        except mysql.connector.Error as error:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la création du compte : {error}")

    def refresh_accounts(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gdn"
            )
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM compte")
            accounts = cursor.fetchall()

            self.table_widget.setRowCount(0)

            for row, account in enumerate(accounts):
                self.table_widget.insertRow(row)

                id_item = QTableWidgetItem(str(account[0]))
                login_item = QTableWidgetItem(account[1])
                role_item = QTableWidgetItem(account[2])

                modify_button = QPushButton("Modifier")
                modify_button.clicked.connect(lambda _, row=row, id=account[0], login=account[1], role=account[2]: self.modify_button_clicked(row, id, login, role))
                self.table_widget.setCellWidget(row, 3, modify_button)

                delete_button = QPushButton("Supprimer")
                delete_button.clicked.connect(lambda _, id=account[0]: self.delete_button_clicked(id))
                self.table_widget.setCellWidget(row, 4, delete_button)

                self.table_widget.setItem(row, 0, id_item)
                self.table_widget.setItem(row, 1, login_item)
                self.table_widget.setItem(row, 2, role_item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la récupération des comptes : {error}")

    def modify_button_clicked(self, row, id, login, role):
        new_login, ok = QInputDialog.getText(self, 'Modifier le login', f'Nouveau login pour "{login}":')
        if ok:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="gdn"
                )
                cursor = connection.cursor()

                query = "UPDATE compte SET login = %s WHERE id = %s"
                cursor.execute(query, (new_login, id))
                connection.commit()
                QMessageBox.information(self, "Succès", f"Le login du compte {login} a été modifié avec succès !")

                cursor.close()
                connection.close()

                # Rafraîchir la liste des comptes après la modification
                self.refresh_accounts()

            except mysql.connector.Error as error:
                QMessageBox.warning(self, "Erreur", f"Erreur lors de la modification du login du compte {login}: {error}")

    def delete_button_clicked(self, id):
        confirmation = QMessageBox.question(self, "Supprimer le compte", "Êtes-vous sûr de vouloir supprimer ce compte ?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="gdn"
                )
                cursor = connection.cursor()

                query = "DELETE FROM compte WHERE id = %s"
                cursor.execute(query, (id,))
                connection.commit()
                QMessageBox.information(self, "Succès", "Le compte a été supprimé avec succès !")

                cursor.close()
                connection.close()

                # Rafraîchir la liste des comptes après la suppression
                self.refresh_accounts()

            except mysql.connector.Error as error:
                QMessageBox.warning(self, "Erreur", f"Erreur lors de la suppression du compte avec ID {id}: {error}")

    def filter_accounts(self):
        search_text = self.search_input.text().lower()
        for row in range(self.table_widget.rowCount()):
            should_show = False
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if item and search_text in item.text().lower():
                    should_show = True
                    break
                widget = self.table_widget.cellWidget(row, col)
                if widget:
                    if isinstance(widget, QPushButton):
                        if search_text in widget.text().lower():
                            should_show = True
                            break
                    elif isinstance(widget, QLineEdit):
                        if search_text in widget.text().lower():
                            should_show = True
                            break
            self.table_widget.setRowHidden(row, not should_show)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ComptePage()
    window.show()
    sys.exit(app.exec_())