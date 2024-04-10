import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

class RecuperationComptePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Récupération de compte email")
        self.setGeometry(100, 100, 400, 300)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Récupération de compte email")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        layout.addWidget(title_label)

        email_label = QLabel("Veuillez entrer l'adresse email associée à votre compte :")
        layout.addWidget(email_label)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Votre adresse email")
        layout.addWidget(self.email_input)

        send_code_button = QPushButton("Envoyer un code de récupération")
        send_code_button.setStyleSheet("padding: 10px 20px; font-size: 16px; font-weight: bold; border-radius: 25px; background-color: #F4D03F; color: white;")
        send_code_button.clicked.connect(self.send_recovery_code)
        layout.addWidget(send_code_button)

        self.message_label = QLabel("")
        self.message_label.setStyleSheet("font-size: 16px; color: green;")
        layout.addWidget(self.message_label)

        self.setLayout(layout)

    def send_recovery_code(self):
        email = self.email_input.text()

        # Générer un code de récupération aléatoire
        recovery_code = str(random.randint(100000, 999999))

        # Configuration des informations de connexion SMTP
        smtp_host = "smtp.example.com"  # Remplacer par le serveur SMTP
        smtp_port = 587  # Port SMTP (par défaut : 587)
        smtp_username = "your_smtp_username"  # Remplacer par votre nom d'utilisateur SMTP
        smtp_password = "your_smtp_password"  # Remplacer par votre mot de passe SMTP

        try:
            # Création de l'e-mail
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = email
            msg['Subject'] = "Code de récupération de compte"

            # Corps de l'e-mail
            message = f"Votre code de récupération est : {recovery_code}"
            msg.attach(MIMEText(message, 'plain'))

            # Connexion au serveur SMTP
            server = smtplib.SMTP(smtp_host, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            # Envoi de l'e-mail
            server.sendmail(smtp_username, email, msg.as_string())
            server.quit()

            # Afficher un message de confirmation
            self.message_label.setText("Le code de récupération a été envoyé à votre adresse e-mail.")

        except Exception as e:
            # Afficher une erreur en cas d'échec de l'envoi de l'e-mail
            QMessageBox.warning(self, "Erreur", f"Erreur lors de l'envoi du code de récupération : {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecuperationComptePage()
    window.show()
    sys.exit(app.exec_())
