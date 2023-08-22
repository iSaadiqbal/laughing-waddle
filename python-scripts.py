import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient_emails):
    sender_email = "saadiqbalbutt89@gmail.com"
    sender_password = "slmoutqfqdwmbzui"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipient_emails)  # Concatenate email addresses

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", e)

# Get the result of the DNS record update from the previous step
dns_result = """
DNS record updated by workflow. Trigger count: 5
"""

# List of recipient email addresses
recipient_emails = ["saad89.linux@gmail.com", "usamashahid3565@gmail.com", "tayyubtahir87@gmail.com"]

# Extract DNS details from your workflow
zone_id = "38b42bfdb42dbe301b6b1a27b86ac939"
record_name = "saad.karazo.com"
record_type = "CNAME"
record_content = "192.168.18.250"
ttl = 3600

# Construct the email subject and body
trigger_count = 5  # Replace with the actual trigger count from the workflow
email_subject = f"DNS Record Update Result - Trigger count: {trigger_count}"
email_body = f"{dns_result}\n\n"
email_body += f"Zone ID: {zone_id}\nRecord Name: {record_name}\nRecord Type: {record_type}\n"
email_body += f"Record Content: {record_content}\nTTL: {ttl}"

# Call the send_email function
send_email(email_subject, email_body, recipient_emails)
