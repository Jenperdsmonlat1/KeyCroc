# KeyCroc
A persistent keylogger which can take screenshot.


This tools is usually for pentest and always in development I'm not responsible for what you will do with this.


Usage:


Before you need to create a database with mysql.

for example:

"CREATE DATABASE name_of_your_database;"

After you need to create an user with all privileges access:

"CREATE USER 'name_of_user'@'localhost' IDENTIFIED BY 'password_user';"

"GRANT ALL PRIVILEGES ON *.* TO 'your_user'@'localhost';"

"FLUSH PRIVILEGES;"

After you need to modify the index.php file by adding the name of your db, the user and the password.
Put the report file on your webserver.

To finish work with python.
Install all necessary librairies with the following command:

py -m pip install -r requierments.txt

after you can start the program with the command:
py main.py

I recommand to use this tools on Windows because it wasn't test on other distro.

A GUI is open click on the button "Commencer" and complete the form with the correcte informations.

Warning:
You need to enable "Allow less secure applications" with your account. Else the keylogger don't start.


Have a good pentest.
