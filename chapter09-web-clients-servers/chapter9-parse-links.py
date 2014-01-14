#!/usr/bin/env python

from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen
from urllib.parse import urljoin

#from BeautifulSoup import BeautifulSoup, SoupStrainer
#from html5lib import parse, treebuilders

URLS = (
    'http://python.org',
#    'http://google.com',
)

def output(x):
    print('\n'.join(sorted(set(x))))
'''
def simpleBS(url, f):
    'simpleBS() - use BeautifulSoup to parse all tags to get anchors'

    parsed = BeautifulSoup(f)
    tags = parsed.findAll('a')
    links = [urljoin(url, tag['href']) for tag in tags]
    output(links)

    #oneliner
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))

    

    >>> from BeautifulSoup import BeautifulSoup as BS
    >>> f = open('pycon.html')
    >>> bs = BS(f)
    >>> type(bs)   # <class 'BeautifulSoup.BeautifulSoup'>
    >>> tags = bs.findAll('a') #returns a list of all <a> tags 
    >>> type(tags) # <type 'list'>
    >>> len(tags)  #  19
    >>> tag = tags[0] # tag = <a href="/2011/">PyCon 2011 Atlanta</a>
    >>> type(tag)     # <class 'BeautifulSoup.Tag'>
    >>> tag['href']   # u'/2011/'


def fasterBS(url, f):
    'fasterBS() - use BeautifulSoup to parse only anchor tags'
    output(urljoin(url, x['href']) for x in BeautifulSoup(
        f, parseOnlyThese=SoupStrainer('a')))

def html5libparse(url, f):
    'html5libparse() - use html5lib to parse anchor tags'
    output(urljoin(url, x.attributes['href']) \
        for x in parse(f) if isinstance(x,
        treebuilders.simpletree.Element) and \
        x.name == 'a')
        
'''
def htmlparser(url, f):
    'htmlparser() - use HTMLParser to parse anchor tags'
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)

def process(url, data):
    '''
    print '\n*** simple BS'
    simpleBS(url, data)
    data.seek(0)
    print '\n*** faster BS'
    fasterBS(url, data)
    data.seek(0)
    print '\n*** HTML5lib'
    html5libparse(url, data)
    '''
    print('\n*** HTMLParser')
    htmlparser(url, data)
    data.seek(0)

def main():
    for url in URLS:
        f = urlopen(url)
        #d= f.read()
        
        data = StringIO(f.read().decode('utf-8'))
        f.close()
        process(url, data)

if __name__ == '__main__':
    main()
