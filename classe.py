import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

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
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title_label)

        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        container_layout.setAlignment(Qt.AlignCenter)

        # Exemple de données statiques pour démonstration
        classes = [
            "Classe A",
            "Classe B",
            "Classe C",
            "Classe D",
            "Classe E",
            "Classe F",
            "Classe G",
            "Classe H"
        ]

        # Parcourir les classes et ajouter chaque bouton à la mise en page
        for class_name in classes:
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
            container_layout.addWidget(class_button)

        layout.addWidget(container_widget)

        return_button = QPushButton("Retour")
        return_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
                background-color: #3498db;
                color: white;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        layout.addWidget(return_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClassListPage()
    window.show()
    sys.exit(app.exec_())
