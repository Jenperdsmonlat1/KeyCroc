import os
import smtplib
import requests
from requests.exceptions import InvalidURL, ConnectionError, ConnectTimeout

class ReportToWebPage:

    def __init__(self, url, smtp_addr, email, password, logger):

        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://127.0.0.1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'http://127.0.0.1/report/',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        self.url = url
        self.smtp_addr = smtp_addr
        self.email = email
        self.password = password
        self.log = logger

    def send_mail_error(self):

        self.serveur = smtplib.SMTP(host=f"{self.smtp_addr}", port=587)
        self.serveur.starttls()
        self.serveur.login(
            user=self.email,
            password=self.password
        )

        self.msg = "Erreur impossible d'envoyer le log veuillez checker votre configuration."
        self.serveur.sendmail(self.email, self.email, self.msg)

    def save_on_computer(self, log):

        self.path = os.getenv('USERPROFILE')

        with open(self.path + "\\AppData\\Temp", "a") as file:
            file.write(log)
            file.close()


    def send_to_db(self, user, log, date, hour):

        self.data = {
            'utilisateur': user,
            'date': date,
            'heure': hour,
            'log': log,
            'submit': 'Valider'
        }

        try:
            self.response = requests.post(url=self.url, headers=self.headers, data=self.data)

        except InvalidURL:
            self.send_mail_error()
            self.save_on_computer(log=self.log)

        except ConnectionError:
            self.save_on_computer(log=self.log)