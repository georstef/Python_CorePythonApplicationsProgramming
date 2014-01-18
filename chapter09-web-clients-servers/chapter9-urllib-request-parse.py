import urllib.request, urllib.parse


if __name__=='__main__':
    #urlopen() returns a file-like object with the response
    f = urllib.request.urlopen('https://www.blogger.com/comment.g?'
                               'blogID=7465480757518241851&'
                               'postID=4588605798694731981&'
                               'isPopup=true')
    #print(f.info())
    #print(f.geturl())
    #print(f.readlines())
    '''
    f.read([bytes]) Reads all or bytes bytes from f
    f.readline()    Reads a single line from f
    f.readlines()   Reads a all lines from f into a list
    f.close()       Closes URL connection for f
    f.fileno()      Returns file number of f
    f.info()        Gets MIME headers of f
    f.geturl()      Returns true URL opened for f
    '''
    #urlretrieve() returns a 2-tuple (filename, mime_hdrs)
    urllib.request.urlretrieve('https://www.blogger.com/comment.g?'
                               'blogID=7465480757518241851&'
                               'postID=4588605798694731981&'
                               'isPopup=true',
                               filename='retrieved_data.txt',
                               reporthook=print,#function to call after each block
                               data=None)
    
    #quote() returns string valid for url (without special characters)
    s = urllib.parse.quote('http://www/~foo/cgi-bin/s.py?name=joe mama&num=6')
    print('quoted: ', s)

    #quote() returns string valid for url (without special characters)
    s = urllib.parse.unquote(s)
    print('unquoted: ', s)

    #quote() takes a dict and returns a string valid for the "query" part
    s = urllib.parse.urlencode({ 'name': 'Georgina Garcia', 'hmdir': '~ggarcia' })
    print('encoded: ', s)
