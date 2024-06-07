import os


def shutdown():
    """Выключает компьютер под управлением Linux."""
    os.system("sudo shutdown -h now")

def reboot():
    """Перезагружает компьютер под управлением Linux."""
    os.system("sudo reboot")