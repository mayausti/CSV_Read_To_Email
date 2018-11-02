# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:07:04 2018

@author: DataTeam
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
from email import encoders


def open_file():
    while True:
        try:
            fp=input('Please enter a file for processing: ')
            f=open(fp,"r")
            break
        except IOError:
            print('The file  could not be opened. Check to make sure that you entered the correct filename')
    return f

def read_file(f):
    name_email_tuple=[]
    count=0
    for line in f:
        if count>=1:
            line=line.split(',')
            email=line[5]
            name_email_tuple.append(email)
            count+=1
        else:
            count+=1
            continue
    return name_email_tuple
def write_email(list_1):
    string_list = ",".join(list_1)#converts list to a comma seperated list
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email', "HelloWorld2018")
    msg = MIMEMultipart()
    msg['From'] = 'name'
    msg['To'] = string_list
    msg['Subject'] = 'Precinct Information'
    body=("""\
    <html>
    <head>
	<title></title>
    </head>
    <body>
    	<p>
        	Whatever You want to address this group as,
	   </p>

      <p>
          line1
      </p>

	  <P>
    		line2 with link <a href="custom link"</a>. more text <mark><b>bold text</b></mark> more text
     </p>

	 

	<p>
    		whatever you want to end the email on
	</p>
	<p>


    		Your Name<br>
             position
             <b>Company</b><.br>
             phone number
	</p>
</body>
</html>""")#html formats it in html
    msg.attach(MIMEText(body,'html'))
    f1="EDO Guidebook 2018.pdf"
    f2="EDO November Training slides.pdf"
    f3="Credentials.pdf"
    attachment_1 = open(f1,'rb')
    attachment_2 = open(f2,'rb')
    attachment_3 = open(f3,'rb')
    part_1 = MIMEBase('application', 'octet-stream')
    part_2 = MIMEBase('application', 'octet-stream')
    part_3 = MIMEBase('application', 'octet-stream')
#adds attachments to emails
 #-----------------------------------------------------------------------------   
    part_1.set_payload(attachment_1.read())
    encoders.encode_base64(part_1)
    part_1.add_header('Content-Disposition',"attachment; filename= "+f1)
    msg.attach(part_1)
#------------------------------------------------------------------------------
    part_2.set_payload(attachment_2.read())
    encoders.encode_base64(part_2)
    part_2.add_header('Content-Disposition',"attachment; filename= "+f2)
    msg.attach(part_2)
#------------------------------------------------------------------------------
    part_3.set_payload(attachment_3.read())
    encoders.encode_base64(part_3)
    part_3.add_header('Content-Disposition',"attachment; filename= "+f3)
    msg.attach(part_3)
#------------------------------------------------------------------------------
    
    text=msg.as_string()
    server.sendmail('email',"list of emails to send mail merge to", text)
    print("Email successfully sent.")
    server.quit()
def main():
    fp=open_file()
    start=read_file(fp)
    write_email(start)
    
if __name__ == "__main__":
    main()