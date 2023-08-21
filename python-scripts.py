import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess

# Replace placeholders with your actual values
gmail_email = "your@gmail.com"
gmail_password = "your_gmail_app_password"  # Generate an app password from your Google Account settings
to_email = "recipient@email.com"

# Run the jq command to format DNS records details
dns_records = subprocess.run(["jq", ".", "dns_records.json"], capture_output=True, text=True).stdout

# Create the email message
message = MIMEMultipart()
message["From"] = gmail_email
message["To"] = to_email
message["Subject"] = "DNS Records Information"

# Attach the formatted DNS records to the email body
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
