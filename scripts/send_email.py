import smtplib
from email.mime.text import MIMEText

# Email configuration
sender_email = "saadiqbalbutt89@gmail.com"
receiver_email = "saad89.linux@gmail.com"
subject = "Static Website HTML"

# Read HTML content from index.html
with open("index.html", "r") as html_file:
    html_content = html_file.read()

# Create the MIMEText object
msg = MIMEText(html_content, "plain")
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, "tfopioxgqjchiuuu")  # Use an app-specific password or OAuth token
    server.sendmail(sender_email, receiver_email, msg.as_string())
