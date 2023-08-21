import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender_email = "saadiqbalbutt89@gmail.com"
    sender_password = "slmoutqfqdwmbzui"
    recipient_email = "saad89.linux@gmail.com"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", e)

# Replace placeholders with your actual values
CF_API_TOKEN = "HsoabgfSbNQVeHpg30hI14GOo8mZLixzk_7HhJY8"
RECORD_NAME = "saad.karazo.com"
RECORD_TYPE = "CNAME"
RECORD_CONTENT = "192.168.18.250"
TTL = 3600
DNS_COMMENT = "Domain verification record"
COMMIT_COUNT = 5  # Replace with the actual commit count

# Construct the DNS record details
dns_details = f"""
DNS record details:
Name: {RECORD_NAME}
Type: {RECORD_TYPE}
IP Address: {RECORD_CONTENT}
TTL: {TTL}
DNS Comment: {DNS_COMMENT}
"""

# Get the result of the DNS record update from the previous step
dns_result = f"DNS record updated by workflow. Commit count: {COMMIT_COUNT}"

# Combine the details and result
email_body = f"{dns_details}\n\n{dns_result}"

# Construct the email subject with commit count
email_subject = f"DNS Record Update Result - Commit {COMMIT_COUNT}"

# Call the send_email function with the subject and body
send_email(email_subject, email_body)
