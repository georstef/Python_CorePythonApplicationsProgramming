#from ftplib import FTP
import ftplib
import os

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    #find ftp host
    try:
        f = ftplib.FTP(HOST)
    except (ftplib.socket.error, ftplib.socket.gaierror) as e:
        print('[ERROR: cannot reach "{0}"]'.format(HOST))
        return
    print('[Connected to host "{0}"]'.format(HOST))

    #login
    try:
        f.login()#server is for anonymous only else it would be (usr, psw)
    except ftplib.error_perm:
        print("[ERROR: cannot login anonymously]")
        f.quit()
        return
    print('[Logged in as "anonymous"]')

    #go to specific directory
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print("[ERROR: cannot CD to '{0}']".format(DIRN))
        f.quit()
        return
    print('[Changed to "{0}" folder]'.format(DIRN))

    #download/retrieve specific file
    try:
        local_file = open(FILE, 'wb')
        f.retrbinary('RETR {0}'.format(FILE), local_file.write)
    except ftplib.error_perm:
        print('[ERROR: cannot read file "{0}"]'.format(FILE))
        local_file.close()
        os.unlink(FILE)#delete the file because (open) creates it empty
    else:
        print('[Downloaded "{0}" to {1}]'.format(FILE, os.getcwd()))
        local_file.close()
        f.quit()
        return

if __name__=='__main__':
    main()
