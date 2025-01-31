import notify2
import os
import pwd
import sys

APP_NAME = "SAVT AGENT"


def get_uid_by_username(username):
    try:
        user_info = pwd.getpwnam(username)
        return user_info.pw_uid
    except KeyError:
        return None

def notify(title, text):
    username    = os.getenv('USER')
    uid         = get_uid_by_username(username)
    if uid is not None:
        os.environ['DBUS_SESSION_BUS_ADDRESS'] = f'unix:path=/run/user/{uid}/bus'

    notify2.init(APP_NAME)
    notification = notify2.Notification(title, text)
    notification.set_timeout(notify2.EXPIRES_NEVER)
    notification.show()




def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    title   = sys.argv[1]
    text    = sys.argv[2]

    notify(title, text)

if __name__ == "__main__":
    main()
