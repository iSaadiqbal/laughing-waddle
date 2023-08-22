import os
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient_emails):
    sender_email = "saadiqbalbutt89@gmail.com"
    sender_password = "slmoutqfqdwmbzui"

    msg = MIMEText(body)
    msg["Subject"] = f"{subject} - Trigger Count: {trigger_count}"
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipient_emails)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", e)

# Get the result of the DNS record update from the previous step
dns_result = f"""
DNS record updated by workflow. Trigger count: {trigger_count}

DNS Details: {os.environ.get("DNS_DETAILS", "N/A")}
"""

# Get the trigger count from the environment variables
trigger_count = int(os.environ.get("GITHUB_RUN_NUMBER", 0))

# List of recipient email addresses
recipient_emails = ["saad89.linux@gmail.com"]

# Call the send_email function
send_email("DNS Record Update Result", dns_result, recipient_emails)
