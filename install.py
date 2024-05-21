import subprocess
import os
import shutil
import pwd
import grp



def create_system_user(username):
    success = False

    try:
        subprocess.run(['sudo', 'useradd', '-r', username], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при создании системного пользователя {username}\n")
        print(f"Exception: {e}")

    else:
        success = True

    finally:
        return success



def add_user_to_sudoers(username):
    success = False

    try:
        with open('/etc/sudoers', 'a') as sudoers_file:
            sudoers_file.write(f"\n{username}\tALL=(ALL) NOPASSWD: ALL\n")

    except Exception as e:
        print(f"Ошибка при добавление пользователя {username} в sudoers\n")
        print(f"Exception: {e}")

    else:
        success = True

    finally:
        return success



def create_directory(directory_path):
    success = False

    try:
        os.makedirs(directory_path)

    except Exception as e:
        print(f"Ошибка при создании директории {directory_path}\n")
        print(f"Exception: {e}")

    else:
        success = True

    finally:
        return success



def change_ownership_recursive(directory_path, user, group=None):
    success = False

    user_id = pwd.getpwnam(user).pw_uid

    if group:
        group_id = grp.getgrnam(group).gr_gid
    else:
        group_id = -1  

    try:
        os.chown(directory_path, user_id, group_id)

        for root, dirs, files in os.walk(directory_path):
            for d in dirs:
                os.chown(os.path.join(root, d), user_id, group_id)
            for f in files:
                os.chown(os.path.join(root, f), user_id, group_id)

    except Exception as e:
        print(f"Произошла ошибка при изменении владельца директории и её содержимого: {e}")
    
    else:
        success = True
    
    finally:
        return success
    



def copy_directory_contents(source_dir, destination_dir):
    success = False

    try:
        shutil.copytree(source_dir, destination_dir)

    except Exception as e:
        print(f"Произошла ошибка при копировании содержимого из директории {source_dir} в директорию {destination_dir}")
        print(f"Exception: {e}")

    else:
        success = True
    
    finally:
        return success
    


def create_systemd_service_file(service_name, content):
    success = False

    try:
        file_path = f"/lib/systemd/system/{service_name}.service"
        with open(file_path, 'w') as service_file:
            service_file.write(content)
        
    except Exception as e:
        print(f"Произошла ошибка при создании файла службы: {e}")
    
    else:
        success = True
    
    finally:
        return success



def enable_service(service_name):
    success = False

    try:
        # Перезагрузка настроек демонов
        reload_process = subprocess.Popen(['systemctl', 'daemon-reload'])
        reload_process.wait()

        # Добавление в автозапуск
        enable_process = subprocess.Popen(['systemctl', 'enable', service_name])
        enable_process.wait()

        # Запуск демона
        start_process = subprocess.Popen(['systemctl', 'start', service_name])
        start_process.wait()


    except Exception as e:
        print(f"Произошла ошибка при управлении сервисом: {e}")
    
    else:
        success = True
    
    finally:
        return success


SOURCE_DIR      = "./notif" #"/home/greg/Documents/pyqt/notif"
APP_DIR         = "/savt"
USER_NAME       = "savtagent"
SERVICE_NAME    = "savtd"

SERVICE_CONTENT = f"""
[Unit]
Description=Test SAVT Agent
After=network.target

[Service]
Type=simple
User={USER_NAME}
WorkingDirectory={APP_DIR}
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
"""


if __name__ == "__main__":
    create_system_user(USER_NAME)
    add_user_to_sudoers(USER_NAME)
    #create_directory(APP_DIR)

    copy_directory_contents(SOURCE_DIR, APP_DIR)  # сам создает указанную директорию
    change_ownership_recursive(APP_DIR, USER_NAME)
    
    create_systemd_service_file(SERVICE_NAME, SERVICE_CONTENT)
    enable_service(SERVICE_NAME)


