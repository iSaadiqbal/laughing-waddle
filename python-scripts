import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Replace placeholders with your actual values
gmail_email = "saadiqbalbutt89@gmail.com"
gmail_password = "slmoutqfqdwmbzui"  # Generate an app password from your Google Account settings
to_email = "Saad89.linux@gmail.com@email.com"

# Read DNS records from the file
with open("dns_records.json", "r") as file:
    dns_records = file.read()

# Create the email message
message = MIMEMultipart()
message["From"] = gmail_email
message["To"] = to_email
message["Subject"] = "DNS Records Information"

# Format the DNS records for the email body
body = f"""
DNS Records Information:

{dns_records}
"""

# Attach the email body
message.attach(MIMEText(body, "plain"))

# Send the email using Google SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_email, gmail_password)
    server.sendmail(gmail_email, to_email, message.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print("An error occurred:", str(e))
