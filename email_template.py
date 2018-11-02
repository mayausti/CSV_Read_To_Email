# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:21:52 2018

@author: DataTeam
"""

"""
Created on Wed Oct 17 15:36:23 2018

@author: DataTeam
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
from email import encoders
import time


def open_file():
    while True:
        try:
            fp=input('Please enter a file for processing: ')#asks for a file to process
            f=open(fp,"r")
            break#iff file is found the loop breaks
        except IOError:
            print('The file  could not be opened. Check to make sure that you entered the correct filename')#prints error message and asks for a new file if the file isn't found
    return f
def read_file(file):
    name_email_tuple=[]#starts list
    count=0#starts count
    for line in file:
        if count>=1:#skips first line in file ie identifiers
            line=line.split(',')#splits line by commas
            name=line[0]
            email=line[1]
            pdf=line[2]
            username=line[3]
            passw=line[4]
            loc=line[5]                     #grabs what you want for each person from the file
            address=line[6]
            add2=line[7]
            clerk=line[8]
            numb=line[9]
            info_list=(name,email,pdf,username,passw,loc,address,add2,clerk,numb)#adds what you want to the list
            name_email_tuple.append(info_list) #adds list to tuple
            count+=1
        else:
            count+=1
            continue
    return name_email_tuple
def write_email(list_1):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #starts server
    server.login('email', 'password')
    missend_list = []
    for tup in list_1:
        try:
            msg = MIMEMultipart()
            msg['From'] = 'Your Name'
            msg['To'] = 'Recipients Name'
            msg['Subject'] = 'Standard Subject'
            b1="whatever you want your message to be HTML is an option for formatting"
            msg.attach(MIMEText(b1,'plain'))#attaches message
            attachment_1 = open(tup[2],'rb')#opens an attachment
            part_1 = MIMEBase('application', 'octet-stream')#starts attachment process by adding a stream
            part_1.set_payload(attachment_1.read())#reads the attachment
            encoders.encode_base64(part_1)#encodes the attachment
            part_1.add_header('Content-Disposition',"attachment; filename= "+tup[2])#adds header to the email attachment
            msg.attach(part_1)#attaches attachment
            text=msg.as_string()#converts message to a stream
            server.sendmail('Your Email', "Recipients Email or A List of Emails" , text)
            print("Email successfully sent.")
            time.sleep(1)#sends new email every one sec
        except smtplib.SMTPRecipientsRefused: #if email doesnt go through
            print('faulty email')
            missend_list.append(tup[1])#adds email to a list
            continue
    server.quit()
    with open('fail.txt','w') as f:
        for item in missend_list:
            f.write("%s\n"%item)#writes all the failed emails to a text file
    print(missend_list)
    
def main():
    fp=open_file()
    start=read_file(fp)
    write_email(start)
    
if __name__ == "__main__":
    main()