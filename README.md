# laughing-waddle (Select the VIEW in CODE for better )

#For email i used this code whoch i got from the Static Email workflow format in the Github
  
    - name: Send Email
        uses: dawidd6/action-send-mail@v3
        with:
          server_address: smtp.gmail.com
          server_port: 587
          username: ${{ secrets.GMAIL_USERNAME }}
          password: ${{ secrets.GMAIL_PASSWORD }}
          subject: "Static Website HTML"
          from: saadiqbalbutt89@gmail.com
          to: saad89.linux@gmail.com
          body:

 THIS works great 



# I created index.html in the master branch ( Repo root ) and used it as my website AND for 
# adding HTML code of the website in the body of the EMAIL i tried different formats in the workflow yml file. 






  

#  1. - name: Read HTML File
        run: |
          html_content=$(cat index.html)
          echo "::set-output name=content::$html_content"
        id: read-html
      **  in the body of email**
            ${html_content}





# 2.    - name: Generate HTML
        working-directory: .
        run: cat index.html > generated_html.html
    ** in email body **
         $(cat generated_html.html)




# 3.   trying with base 64 encoding
    - name: Read HTML File
        id: read-html
        run: |
          html_content=$(cat index.html | base64 -w 0)
          echo "::set-output name=content::$html_content"
    **   in the email body**
      <iframe srcdoc="${{ steps.read-html.outputs.content }}" frameborder="0" width="100%" height="500"></iframe>


# 4  - name: Read HTML File
        id: read-html
        run: |
          html_content=$(cat index.html)
          echo "::set-output name=content::$html_content"


        **in the email body **
        body: ${{ steps.read-html.outputs.content }}

none of them worked!!!


Then i tried adding the HTML code of the webiste in the email body with python, i added the .py file in the repo (/scripts/send_email.py)
and used the same for email and converted it in python 


# setting the environment for the email, giving some peramteres
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText  



#My Email configuration 
sender_email = "saadiqbalbutt89@gmail.com"
receiver_email = "tayyubtahir87@gmail.com"
subject = "Static Website HTML"

# Now opening the file contents and making it readable, this makes an object with the html content which is equal to
# html_file(variable)and the read the that variable which has the content as well with ".read()" and it also converts it in a string as well
with open("index.html", "r") as html_file:
  html_content = html_file.read()

# Additional text has a format and a style that we have to follow - 
additional_text = """
Hello, I am using python file to add HTMl code in the body of the email. I tried with many workflow formatts from the
github none of them worked with the HTML i was not able to add it in the email body.  so i found a way to do it through the python code.
then i learned how to make my .py file work with the yaml file. 
and now i have the HTML code of the site below as text.

---

{}

---

Thank you,
Saad
""".format(html_content)

# Create the MIMEText object
msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Attach additional text to the email body
msg.attach(MIMEText(additional_text, "plain"))

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, "tfopioxgqjchiuuu") 
    server.sendmail(sender_email, receiver_email, msg.as_string())
