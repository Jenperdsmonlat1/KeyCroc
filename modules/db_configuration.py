import sqlite3
from rich.console import Console

console = Console()


class DbConfiguration:

    def __init__(self):
        self.db = sqlite3.connect("configuration.db")
        self.cursor = self.db.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXIST configuration(
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            smtpaddr VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NUL,
            url VARCHAR(255) NOT NULL,
            interval INT
        )
        """)
        self.db.commit()

    def insert_data(self, smtp, email, password, url, interval, name):

        self.smtp_addr = smtp
        self.password = password
        self.email = email
        self.url = url
        self.interval = interval
        self.name = name

        self.data = {
            "email": self.email,
            "smtpaddr": self.smtp_addr,
            "password": self.password,
            "url": self.url,
            "interval": self.interval,
            "name": self.name
        }

        self.cursor.execute("""
        INSERT INTO configuration(email, smtpaddr, password, url, interval) 
        VALUES(:email, :smtpaddr, :password, :url, :interval)""", self.data)

    def check_data(self, var_email, var_smtp_addr, var_password, var_interval, var_url):

        self.var_email = var_email,
        self.var_smtp = var_smtp_addr
        self.var_password = var_password,
        self.var_interval = var_interval
        self.var_url = var_url

        self.var_email = self.cursor.execute("""
        SELECT email FROM configuration""")

        self.var_smtp = self.cursor.execute("""
        SELECT smtpaddr FROM configuration""")

        self.var_password = self.cursor.execute("""
        SELECT password FROM configuration""")

        self.var_interval = self.cursor.execute("""
        SELECT interval FROM configuration""")

        self.var_url = self.cursor.execute("""
        SELECT url FROM configuration""")