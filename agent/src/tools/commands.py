import subprocess
import os

NOTIFICATION_SCRIPT = "./src/tools/notification.py"
PYTHON_PATH = "/usr/bin/python3"



def notification(title, text):
    """
    TODO
    Добавить получение списка всех активных пользователей и вызов уведомлений для каждого из них
    """
    username = "greg"
    
    subprocess.run(["sudo", "-u", username, PYTHON_PATH, NOTIFICATION_SCRIPT, f'{title}', f'{text}'], 
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def shutdown():
    """Выключает компьютер под управлением Linux."""
    os.system("sudo shutdown -h now")

def reboot():
    """Перезагружает компьютер под управлением Linux."""
    os.system("sudo reboot")
