import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox, QStackedWidget, QFormLayout
from PyQt5.QtCore import Qt

class InscriptionProfesseurApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inscription Professeur")
        self.setGeometry(100, 100, 600, 400)

        self.stacked_widget = QStackedWidget()

        self.personal_info_widget = QWidget()
        self.professional_info_widget = QWidget()

        self.init_personal_info_ui()
        self.init_professional_info_ui()

        self.stacked_widget.addWidget(self.personal_info_widget)
        self.stacked_widget.addWidget(self.professional_info_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

    def init_personal_info_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()
        self.situation_matrimoniale_combobox = QComboBox()
        self.situation_matrimoniale_combobox.addItems(["Marié(e)", "Célibataire"])
        self.lieu_naissance_input = QLineEdit()
        self.date_naissance_input = QLineEdit()

        form_layout.addRow("Nom :", self.nom_input)
        form_layout.addRow("Prénom :", self.prenom_input)
        form_layout.addRow("Situation matrimoniale :", self.situation_matrimoniale_combobox)
        form_layout.addRow("Lieu de naissance :", self.lieu_naissance_input)
        form_layout.addRow("Date de naissance :", self.date_naissance_input)

        self.personal_info_submit_button = QPushButton("Valider")
        self.personal_info_submit_button.clicked.connect(self.handle_personal_info_submit)

        layout.addLayout(form_layout)
        layout.addWidget(self.personal_info_submit_button)
        self.personal_info_widget.setLayout(layout)

    def init_professional_info_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.diplome_formation_input = QLineEdit()
        self.autre_diplome_input = QLineEdit()
        self.matieres_enseignees_input = QLineEdit()
        self.autre_matiere_input = QLineEdit()

        form_layout.addRow("Diplôme de formation :", self.diplome_formation_input)
        form_layout.addRow("Autre diplôme :", self.autre_diplome_input)
        form_layout.addRow("Matières enseignées :", self.matieres_enseignees_input)
        form_layout.addRow("Autre matière :", self.autre_matiere_input)

        self.professional_info_submit_button = QPushButton("Valider")
        self.professional_info_submit_button.clicked.connect(self.handle_professional_info_submit)

        layout.addLayout(form_layout)
        layout.addWidget(self.professional_info_submit_button)
        self.professional_info_widget.setLayout(layout)

    def handle_personal_info_submit(self):
        # Traitement des informations personnelles
        QMessageBox.information(self, "Succès", "Informations personnelles soumises avec succès.")
        # Vous pouvez ajouter ici le code pour enregistrer les informations dans une base de données par exemple
        # Redirection vers la prochaine étape du formulaire
        self.stacked_widget.setCurrentIndex(1)

    def handle_professional_info_submit(self):
        # Traitement des informations professionnelles
        QMessageBox.information(self, "Succès", "Informations professionnelles soumises avec succès.")
        # Vous pouvez ajouter ici le code pour enregistrer les informations dans une base de données par exemple
        # Redirection vers une page de confirmation ou une autre action
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InscriptionProfesseurApp()
    window.show()
    sys.exit(app.exec_())
