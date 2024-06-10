import os
import sys
import subprocess
from ._collectors   import ActiveUsersCollector

main_file_path = os.path.abspath(sys.argv[0])
main_file_dir  = os.path.dirname(main_file_path)

NOTIFICATION_SCRIPT = f"{main_file_dir}/scripts/notification.py"
PYTHON_PATH         = "/usr/bin/python3"




class Notificator:
    def __init__(self, title:str, text:str, username=""):
        self._title     = title
        self._text      = text
        self._user      = username


    def _notificate_user(self, username):      
        os.system(f"sudo -u {username} {PYTHON_PATH} {NOTIFICATION_SCRIPT} {self._title} {self._text}")
        # try:
        #     subprocess.run(
        #         args    = ["sudo", "-u", "greg", PYTHON_PATH, NOTIFICATION_SCRIPT, self._title, self._text],
        #         stdout  = subprocess.PIPE, 
        #         stderr  = subprocess.PIPE, 
        #         text    = True)
        # except subprocess.SubprocessError as e:
        #     raise Exception(e)

    def notify(self):
        if not self._user:
            for user in ActiveUsersCollector().collect():
                self._notificate_user(user)
        else:
            self._notificate_user(self._user)