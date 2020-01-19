import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Gourav Singh'
email['to'] = 'hashir.imam99@gmail.com'
email['subject'] = 'you are gate 2020 topper!!'

email.set_content('you just have to give me a party !!')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('gsingh6122016@gmail.com', 'qtxkuqkgmzqbvcty')
    smtp.send_message(email)
    print('all good boss!')
