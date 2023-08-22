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
DNS record updated by workflow. Trigger count: $GITHUB_RUN_NUMBER
DNS details:
Record Name: saad.karazo.com
Record Type: CNAME
Record Content: YOUR_IP_ADDRESS
TTL: 3600
Comment: Domain verification record
"""

# List of recipient email addresses
recipient_emails = ["saad89.linux@gmail.com"]

# Call the send_email function
send_email("DNS Record Update Result (Trigger #$GITHUB_RUN_NUMBER)", dns_result, recipient_emails)
