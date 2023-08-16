import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email():
    try:
        # Set email details
        sender_email = 'saadiqbalbutt89@gmail.com'
        recipient_email = 'saad89.linux@gmail.com'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_password = os.environ.get('slmoutqfqdwmbzui')  # Use the environment variable

        subject = 'Check Out My Website!'
        website_link = 'https://isaadiqbal.github.io/laughing-waddle/'

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Set the email body
        body = f"Bonsoir,\n\nPlease check out my website: {website_link}\n\nBest regards,\KING KONG"

        # Attach the body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    send_email()
