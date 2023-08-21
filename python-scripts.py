import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender_email = "saadiqbalbutt89@gmail.com"
    sender_password = "slmoutqfqdwmbzui"
    recipient_email = "saad89.linux@gmail.com"  # Update with recipient's email address

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

# Get the result of the DNS record update from the previous step
dns_result = """
DNS record updated by workflow. Commit count: 5
"""

# Call the send_email function
send_email("DNS Record Update Result", dns_result)
