from smtplib import SMTP
from poplib import POP3

USERNAME = 'xxxxx@xxxxx.xx'
PASSWORD = 'xxxxxxx'

def send_mail(host, username, password):
    print("sending mail.....")
    s = SMTP(host)
    s.login(username, password)
    s.sendmail(username,
               username, # here we can place a list of recipients
               "\r\n"
               "From: {0}\r\n"
               "To: {0}\r\n"
               "Date: today\r\n"
               "Subject: Test\r\n\r\n"
               "Let's see if this works\r\n".format(username))
    s.quit()
    return True


def receive_mail(host, username, password):
    p = POP3(host)
    p.user(username)
    p.pass_(password)

    mail_id = 0
    print("waiting for mail to appear.", end='')
    while mail_id == 0:
        print(".", end='')
        mail_id = p.stat()[0]
    print(".") # just for line break
    rsp, msg, siz = p.retr(mail_id)
    p.dele(mail_id) # mark for deletion
    p.quit() # log out (also deletes marked mail)
    for line in msg:
            print(line.decode())
    

if __name__=="__main__":
    # send a mail to myself (SMTP)
    if send_mail('xxxxxxx.xxxxxxx.xx', USERNAME, PASSWORD):
        print("mail sent...")
        # receive the mail (POP3)
        receive_mail('xxxx.xxxxxx.xx', USERNAME, PASSWORD)
