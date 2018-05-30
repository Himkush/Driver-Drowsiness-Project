import smtplib
import datetime
from time import ctime

currentDT = datetime.datetime.now()
string1 =  ctime()
host = "smtp.gmail.com"
port = 587
username = "codebreakerraj@gmail.com"
password = "rajan.08"
from_email = username
to_list = ["himkushwaha08@gmail.com", "kushhim@outlook.com"]

##email_conn = smtplib.SMTP(host, port)
##email_conn.ehlo()
##email_conn.starttls()
##email_conn.login(username, password)
##email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
##email_conn.quit()


from smtplib import SMTP

def send_sms():
    from smtplib import SMTP

    ABC = SMTP(host, port)
    
    ABC.ehlo()
    ABC.starttls()
    ABC.login(username, password)
    ABC.sendmail(from_email, to_list, "Alert your driver was sleeping!" + "\n" + string1)
    ABC.quit()


    from smtplib import SMTP, SMTPAuthenticationError, SMTPException


    pass_wrong = SMTP(host, port)   
    pass_wrong.ehlo()
    pass_wrong.starttls()
    try:
        pass_wrong.login(username, "wrong_password")
        pass_wrong.sendmail(from_email, to_list, "Alert your driver was sleeping")
    except SMTPAuthenticationError:
         print("No internet connectivity message not send")
         pass
    except:
        print("an error occured")

    pass_wrong.quit()
