import smtplib
from email.mime.text import MIMEText

def send_alert(subject, message, recipient_email):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmali.com'
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.send_message(msg)