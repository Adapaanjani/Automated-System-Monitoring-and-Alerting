# 🚨 **Automated System Monitoring & Alerting** 🚨

This project monitors your system's **CPU** and **RAM** usage in real time and sends **alerts** if the usage exceeds a predefined threshold. It includes a **real-time web dashboard** to display system performance and sends notifications via **Email**, **Slack**, and **Telegram** when the usage goes beyond the set limits.

## Features ✨
- **Real-Time System Monitoring** 🖥️
- **Web Dashboard** to display CPU and RAM usage 📊
- **Email**, **Slack**, and **Telegram** notifications 🚨
- **Logs** for system monitoring and errors 📂
- **Threshold Alerts** for CPU/RAM usage above 80% ⚠️

## Requirements 🛠️
To get started, you’ll need:
- **Python 3.x** 🐍
- `psutil` (to monitor system stats) 📊
- `requests` (for sending notifications) 📩
- `Flask` (for the web dashboard) 🌐
- `Chart.js` (for displaying real-time graphs) 📈

To install the dependencies, run:

```bash
pip install psutil requests Flask
```

## Setup ⚙️
### 1. Clone the Repository
Download or clone the project files to your local machine.

### 2. Configure Alerts 🚨
- **Email Alerts**: Set your sender and receiver email details in the `send_alert()` function. Use an **App Password** if you're using **Gmail** with **2FA** enabled.
- **Slack Notifications**: Get your **Slack Webhook URL** and update the script.
- **Telegram Notifications**: Set up a **Telegram Bot Token** and **Chat ID**.

### 3. Run the Flask Web Dashboard 💻
Start the Flask server with the following command:

```bash
python app.py
```

This will start the dashboard at `http://127.0.0.1:5000/`.

### 4. Open the Dashboard 🌐
Open a browser and visit `http://127.0.0.1:5000/` to see the real-time system statistics.

## System Monitoring 📊
- **CPU & RAM Usage** are monitored every second.
- If the usage exceeds **80%**, the following notifications are sent:
  - **Email Alert** 📧
  - **Slack Notification** 🧑‍💻
  - **Telegram Alert** 📲

### Notification Example 📢
Here’s an example of what the notification messages will look like:

**📧 Email Alert**:
```
Subject: System Alert

🚨 High CPU Usage Alert: 85%
🚨 High RAM Usage Alert: 90%
```

**🧑‍💻 Slack Notification**:
```
🚨 High CPU Usage Alert: 85%
🚨 High RAM Usage Alert: 90%
```

**📲 Telegram Notification**:
```
🚨 High CPU Usage Alert: 85%
🚨 High RAM Usage Alert: 90%
```

## Real-Time Dashboard 📈
On the **web dashboard**, the CPU and RAM usage are shown in real-time using **Chart.js**. Here’s how it looks:


- **Red Line**: CPU Usage
- **Blue Line**: RAM Usage

The data updates every **3 seconds**.

## Troubleshooting 🔧
- Ensure all required packages are installed using `pip install`.
- Double-check your **Slack Webhook URL**, **Telegram Bot Token**, and **Email credentials**.
- For Gmail, ensure 2FA is enabled and use an **App Password**.
