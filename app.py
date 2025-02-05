import psutil
import smtplib
import json
import logging
import requests
from flask import Flask, render_template, jsonify
import webbrowser
# Configuration
THRESHOLD = 80  # Alert threshold for CPU/RAM
LOG_FILE = "system_monitor.log"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
TELEGRAM_BOT_TOKEN = "7568730918:AAGIuiBthiAv72oZuHX5YiJYHB6jyd1pqRk"
TELEGRAM_CHAT_ID = "5240491483"

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_alert(subject, message):
    sender_email = 'adapaanjani567@gmail.com'
    receiver_email = 'anjaninsssadapa@gmail.com'
    password = 'nzyx ovii zfox jjfz'
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, f'Subject: {subject}\n\n{message}')
        logging.info(f"Email alert sent: {subject}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def send_slack_notification(message):
    try:
        payload = {"text": message}
        requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        logging.info("Slack notification sent.")
    except Exception as e:
        logging.error(f"Failed to send Slack notification: {e}")


def send_telegram_notification(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, data=data)
        logging.info("Telegram notification sent.")
    except Exception as e:
        logging.error(f"Failed to send Telegram notification: {e}")


def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    alert_message = ""

    if cpu_usage > THRESHOLD:
        alert_message += f"High CPU Usage Alert: {cpu_usage}%\n"
    if ram_usage > THRESHOLD:
        alert_message += f"High RAM Usage Alert: {ram_usage}%\n"

    if alert_message:
        send_alert("System Alert", alert_message)
        send_slack_notification(alert_message)
        send_telegram_notification(alert_message)
        logging.warning(alert_message)


# Flask Web Dashboard
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/stats')
def stats():
    data = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory().percent
    }
    return jsonify(data)


if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)
