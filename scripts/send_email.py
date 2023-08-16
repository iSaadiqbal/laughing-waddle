import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_html_email():
    try:
        # Create a message object
        msg = MIMEMultipart()

        # Set email details
        sender_email = 'saadiqbalbutt89@gmail.com'
        recipient_email = 'saad89.linux@gmail.com'

        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'HTML Email Subject'

        # Create the HTML content
        website_link = '<a href="https://isaadiqbal.github.io/laughing-waddle/">Visit our website</a>'
        additional_text = 'Hello, this is an HTML email with a link to our website!'
        html_content = f"<html><body><p>{additional_text}</p><p>{website_link}</p></body></html>"

        # Attach the HTML content to the message
        msg.attach(MIMEText(html_content, 'html'))

        # Connect to the SMTP server and send the email
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        
        email_password = os.environ.get('tfopioxgqjchiuuu')
        if email_password is None:
            raise ValueError("GMAIL_APP_PASSWORD environment variable not set")
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    send_html_email()
