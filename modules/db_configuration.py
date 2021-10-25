import json


class JsonData:

    def __init__(self, json_file):

        self.json_file = json_file

    def write_info(self, interval, smtp_addr, email, password, url_report, nom):

        self.interval = interval
        self.smtp_addr = smtp_addr
        self.email = email
        self.password = password
        self.url = url_report
        self.nom = nom

        with open(self.json_file, "w") as file:

            data = {
                "email": self.email,
                "interval": self.interval,
                "password": self.password,
                "nom": self.nom,
                "smtp_addr": self.smtp_addr,
                "url_page": self.url
            }

            json.dump(data, file)
            file.close()

    def read_info(self, interval, smtp_addr, email, password, url_report, nom):

        self.interval_to_read = interval
        self.smtp_to_read = smtp_addr
        self.email_to_read = email
        self.password_to_read = password
        self.url_to_read = url_report
        self.nom_to_read = nom

        with open(self.json_file, "r") as file:

            json_content = file.read()
            obj_json = json.loads(json_content)

            self.interval_to_read = obj_json['interval']
            self.smtp_to_read = obj_json['smtp_addr']
            self.email_to_read = obj_json['email']
            self.password_to_read = obj_json['password']
            self.url_to_read = obj_json['url_page']
            self.nom_to_read = obj_json['nom']

            file.close()
