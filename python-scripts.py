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
trigger_count = 5  # Replace with the actual trigger count from the workflow
dns_details = "DNS record details: Zone ID, Record Name, Record Type, Record Content, TTL, etc."

# List of recipient email addresses
recipient_emails = ["saad89.linux@gmail.com", "usamashahid3565@gmail.com", "tayyubtahir87@gmail.com"]

# Construct the email subject and body
email_subject = f"DNS Record Update Result - Trigger count: {trigger_count}"
email_body = f"DNS record updated by workflow.\n\nTrigger count: {trigger_count}\n\n{dns_details}"

# Call the send_email function
send_email(email_subject, email_body, recipient_emails)
