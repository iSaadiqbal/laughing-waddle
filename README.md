# laughing-waddle

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




I created index.html in the master branch ( Repo root ) and used it as my website AND for 
adding HTML code of the website in the body of the EMAIL i tried different formats in the workflow yml file. 

  
  
  1. - name: Read HTML File
        run: |
          html_content=$(cat index.html)
          echo "::set-output name=content::$html_content"
        id: read-html
      **  in the body of email**
            ${html_content}



2. 

    - name: Generate HTML
        working-directory: .
        run: cat index.html > generated_html.html

   ** in email body **

   $(cat generated_html.html)



3.

   trying with base 64 encoding
    - name: Read HTML File
        id: read-html
        run: |
          html_content=$(cat index.html | base64 -w 0)
          echo "::set-output name=content::$html_content"
   **   in the email body**
      <iframe srcdoc="${{ steps.read-html.outputs.content }}" frameborder="0" width="100%" height="500"></iframe>


4.   
    - name: Read HTML File
        id: read-html
        run: |
          html_content=$(cat index.html)
          echo "::set-output name=content::$html_content"


        **in the email body **
        body: ${{ steps.read-html.outputs.content }}

none of them worked!!!


Then i tried adding the HTML code of the webiste in the email body with python, i added the .py file in the repo (/scripts/send_email.py)

       
