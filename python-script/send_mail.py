import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail details
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
gmail_password = "your_gmail_password"  # Use an app-specific password or integrate with Gmail API

subject = "Cloudflare DNS Update"
message = """
The Cloudflare DNS record has been updated.

Details:
- DNS Record: {dns_record}
- Comment Count: {comment_count}
- Workflow Run ID: {workflow_run_id}
- Workflow Run URL: {workflow_run_url}
"""

# Replace placeholders with actual values
dns_record = "{{ steps.check-dns.outputs.dns-record }}"
comment_count = "{{ steps.increment-count.outputs.stdout }}"
workflow_run_id = "{{ github.run_id }}"
workflow_run_url = "{{ github.event.repository.html_url }}/actions/runs/${{ github.run_id }}"

message = message.format(dns_record=dns_record, comment_count=comment_count, workflow_run_id=workflow_run_id, workflow_run_url=workflow_run_url)

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, gmail_password)
server.sendmail(sender_email, receiver_email, msg.as_string())
server.quit()
