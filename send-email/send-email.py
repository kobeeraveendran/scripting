# Kobee Raveendran
# sending emails with Python

################################################
#                                              #
# NOTE: In order for this to work,             #
#       enable "Less secure apps"              #
#       at myaccount.google.com/lesssecureapps  #
#                                              #
################################################

import smtplib
# this contains the email address and password; create one and specify
# these fields yourself to login
from config import getEmail, getPassword

def send_email(subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', port = 587)
        server.ehlo()
        server.starttls()

        # login (email and password are in another python file for confidentiality)
        server.login(getEmail(), getPassword())
        msg = 'Subject: {} \n\n{}'.format(subject, message)
        server.sendmail(getEmail(), getEmail(), msg)
        server.close()
        print('Message sent successfully')
    except:
        print('Email failed to send')

subject = "Initial testing"
message = "TESTYTEST"

send_email(subject, message)
