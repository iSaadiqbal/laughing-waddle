import smtplib
from email.mime.text import MIMEText

# Email configuration
sender_email = "your@gmail.com"
receiver_email = "recipient@example.com"
subject = "Static Website HTML"
message = open("index.html").read()

# Create the MIMEText object
msg = MIMEText(message, "html")
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, "your_password")  # Use an app-specific password or OAuth token
    server.sendmail(sender_email, receiver_email, msg.as_string())
