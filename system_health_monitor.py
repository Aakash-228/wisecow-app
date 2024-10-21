# system_health_monitor.py

import psutil
import smtplib
from email.mime.text import MIMEText

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'System Alert'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient_email@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail('your_email@example.com', 'recipient_email@example.com', msg.as_string())

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > CPU_THRESHOLD:
        send_alert(f'CPU usage is above threshold: {cpu_usage}%')

    # Check memory usage
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        send_alert(f'Memory usage is above threshold: {memory_usage}%')

    # Check disk usage
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        send_alert(f'Disk usage is above threshold: {disk_usage}%')

if __name__ == "__main__":
    check_system_health()
