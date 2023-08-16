import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_html_email():
    sender_email = 'saadiqbalbutt89@gmail.com'
    recipient_email = 'saad89.linux@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    email_password = os.environ.get('iekhfkmugclnfzof')

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'HTML Email Subject'

    website_link = '<a href="https://isaadiqbal.github.io/laughing-waddle/">Visit our website</a>'
    additional_text = 'Hello, this is an HTML email with a link to our website!'
    html_content = f"<html><body><p>{additional_text}</p><p>{website_link}</p></body></html>"
    msg.attach(MIMEText(html_content, 'html'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

    print("Email sent successfully!")

if __name__ == "__main__":
    send_html_email()
