from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import server

import smtplib
from xmlrpc.client import ProtocolError

user        = 'shawn@pluribustechnologies.com'
password    = ''
server_name = 'smtp.office365.com'
tcp_port    = 587 
msg         = MIMEMultipart()

msg['from']     = 'shawn@pluribustechnologies.com'
msg['to']       = 'taylorshawn@hotmail.com'
msg['subject']  = 'MOOC Support Test Email'
msg.attach(MIMEText('Support Test Message', 'plain')) 

mailserver = smtplib.SMTP(host=server_name, port=tcp_port)

mailserver.starttls()
mailserver.login(user, password)
mailserver.send_message(msg)
mailserver.quit()
