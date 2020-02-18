import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from pandas import *

text = Template(Path('index.txt').read_text()) 


# from pandas import *
# xls = ExcelFile('my_file.xlsx')
# data = xls.parse(xls.sheet_names[0]).to_dict()
# for i in data['Name']:
#     print(data['Name'][i])
#     print(data['Emails'][i])

xls = ExcelFile('my_file.xlsx')
data = xls.parse(xls.sheet_names[0]).to_dict()

# database = {
#     'Hashir' : 'hashir.imam99@gmail.com',
#     'Probir da' : 'biswasprobir1999@gmail.com',
#     'aniket dutta' : 'datta.aniket@gmail.com'
# }

for i in data['Name']:
    email = EmailMessage()
    email['from'] = 'Gourav Singh'
    email['to'] = data['Emails'][i]
    email['subject'] = 'Hall Day invitation !!'

    email.set_content(text.substitute({'name': data['Name'][i]}))

    with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('gsingh6122016@gmail.com', 'qtxkuqkgmzqbvcty')
        smtp.send_message(email)
        print('all good boss!')
 