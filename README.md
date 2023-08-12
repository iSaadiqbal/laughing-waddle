# laughing-waddle


 
 
 for email 
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


index.html is the website in the root of main branch. 


  trying different methods for showing index.html content in email body
  1. - name: Read HTML File
        run: |
          html_content=$(cat index.html)
          echo "::set-output name=content::$html_content"
        id: read-html
      **  in the body of email**
            ${html_content}




2.     $(cat index.html)  in the body



3.  trying with base 64 encoding
 - name: Read HTML File
        id: read-html
        run: |
          html_content=$(cat index.html | base64 -w 0)
          echo "::set-output name=content::$html_content"
   **   in email body**
      <iframe srcdoc="${{ steps.read-html.outputs.content }}" frameborder="0" width="100%" height="500"></iframe>


4.   
      - name: Read HTML File
        id: read-html
        run: |
          html_content=$(cat index.html)
          echo "::set-output name=content::$html_content"


        **in the email body **
body: ${{ steps.read-html.outputs.content }}

        

       
