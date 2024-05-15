import subprocess
import os



def notification(title, text):
    username = "greg"
    py_file = "./notification.py"
    
    subprocess.run(["sudo", "-u", username, "/usr/bin/python3", py_file, f'"{title}"', f'"{text}"'], 
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def shutdown():
    """Выключает компьютер под управлением Linux."""
    os.system("sudo shutdown -h now")

def reboot():
    """Перезагружает компьютер под управлением Linux."""
    os.system("sudo reboot")
