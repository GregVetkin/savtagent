from flask import Flask, request
from commands import  shutdown, reboot, notification


app = Flask(__name__)


@app.route('/message')
def send_notification():
    title   = request.args.get('title')
    text    = request.args.get('text')
    notification(title, text)

    return "Уведомление отправлено"


@app.route('/shutdown')
def shutdown_pc():
    shutdown()
    return "Сигнал на выключение отправлен"


@app.route('/reboot')
def reboot_pc():
    reboot()
    return "Сигнал на перезагрузку отправлен"


app.run(host='192.168.0.254', port=8080, debug=False)
