#!/usr/bin/env python3

import urllib.request, urllib.error, urllib.parse

LOGIN = 'wesley'
PASSWD = "you'llNeverGuess"
URL = 'http://localhost'
REALM = 'Secure Archive'

def handler_version(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM,
                      urllib.parse.urlparse(url)[1],
                      LOGIN,
                      PASSWD)
    opener = urllib.request.build_opener(hdlr)
    print('HANDLER-> ', hdlr.passwd.passwd)
    urllib.request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = urllib.request.Request(url)
    b64str = encodestring(bytes('%s:%s' % (LOGIN, PASSWD), 'utf-8'))[:-1]
    req.add_header("Authorization", "Basic %s" % b64str)
    return req

for funcType in ('handler', 'request'):
    print('******************')
    print('*** Using %s:' % funcType.upper())
    print('******************')
    url = eval('%s_version' % funcType)(URL)
    print('URL-> ', url)
    f = urllib.request.urlopen(url)
    for line in f.readlines():
        print(str(line, 'utf-8'), end='')
    f.close()
    print('')
