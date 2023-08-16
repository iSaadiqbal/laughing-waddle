import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email():
    # Create a message object
    msg = MIMEMultipart()
    
    # Set email details
    sender_email = 'saadiqbalbutt89@gmail.com'
    recipient_email = 'saad89.linux@gmail.com'
    email_password = 'wuyfxxubulbosjab'
    
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'HTML Email Subject'
    
    # Create the HTML content
    website_link = '<a href="https://isaadiqbal.github.io/laughing-waddle/">Visit our website</a>'
    additional_text = 'Hello, this is an HTML email with a link to our website!'
    #html_content = f"<html><body><p>{additional_text}</p><p>{https://isaadiqbal.github.io/laughing-waddle/}</p></body></html>"
    html_content = f"<html><body><p>{additional_text}</p><p><a href='https://isaadiqbal.github.io/laughing-waddle/'>Visit our website</a></p></body></html>"

    
    # Attach the HTML content to the message
    msg.attach(MIMEText(html_content, 'html'))
    
    # Connect to the SMTP server and send the email
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender_email, email_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

send_html_email()
