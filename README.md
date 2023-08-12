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
          body: |
 
 THIS works great 


  trying different methods for showing index.html content in email body
  1. - name: Read HTML File
        run: |
          html_content=$(cat index.html)
          echo "::set-output name=content::$html_content"
        id: read-html
      **  in the body of email**
            ${html_content}
2. 



       
