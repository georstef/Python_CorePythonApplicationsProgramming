from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from poplib import POP3
import email

USERNAME = 'xxxxx@xxxx.xx'
PASSWORD = 'xxxxxxx'

def make_mime_mail(attachment=""):
    email_ = MIMEMultipart('alternative')
    text = MIMEText('Plain text\r\n', 'plain')
    email_.attach(text) # 1st part (normally the text in html and plain must be the same)

    html = MIMEText('<html><body><h1>HTML text</h1></body></html>',
                    'html')
    email_.attach(html) # 2nd part (normally the text in html and plain must be the same)

    if attachment:
        f = open(attachment, 'rb')
        data = f.read()
        f.close()

        image = MIMEImage(data, name=attachment)
        '''
        # the next line is optional (???)
        image.add_header('Content-Disposition',
                         'attachment; filename={0}'.format(attachment))
        '''
        
        email_.attach(image) # 3rd part (the attachment)
    return email_
    
def send_mime_mail(host, username, password):
    print("sending mail.....")
    s = SMTP(host)
    s.login(username, password)

    # msg = make_mime_mail() # simple mail
    msg = make_mime_mail("chapter3_mime.png") # mail with attachment
    msg['From'] = username
    msg['To'] = username
    msg['Subject'] = 'This is a multipart alternative test mail'

    s.sendmail(username, username, msg.as_string())
    print(msg.as_string())
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

    msg=[x.decode() for x in msg]
    emsg = email.message_from_string('\r\n'.join(msg))
    if emsg.is_multipart():
        for part in emsg.walk():
            print('')
            print(part.get_content_type())
            if part.get_content_type() == 'text/plain':
                print(part.get_payload())
            elif part.get_content_type() == 'text/html':
                print(part.get_payload())
            elif part.get_content_type() == 'image/png':
                print('chapter3_mime_downloaded.png')
                data = part.get_payload(decode=True) # for when it's binary
                f = open('chapter3_mime_downloaded.png', 'wb')
                data = f.write(data)
                f.close()
                

if __name__=="__main__":
    # send a MIME mail to myself (SMTP)
    if send_mime_mail('xxxxxxxx.xxxxx.xx', USERNAME, PASSWORD):
        print("mail sent...")
        # receive the MIME mail (POP3)
        receive_mail('xxxx.xxxxxx.xx', USERNAME, PASSWORD)
