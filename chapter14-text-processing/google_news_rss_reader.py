from io import BytesIO
from urllib.request import urlopen
from pprint import pprint # pretty-print
from xml.etree import ElementTree


def top_news(tree, count=3):
    pair = [None, None]
    for elmt in tree.getiterator():
        # we need the pair 'title' and 'link' but not when
        # the 'title' starts with "Top Stories"
        if elmt.tag == 'title':
            skip = elmt.text.startswith('Top Stories')
            if skip:
                continue # next element
            pair[0] = elmt.text
        if elmt.tag == 'link':
            if skip:
                continue
            pair[1] = elmt.text
            if pair[0] and pair[1]:
                count -= 1
                yield(tuple(pair)) # sends a tuple back to be used
                # and return here (at this line) on the next iteration
                # print('here') <- this is printed between the pretty-prints
                if not count:
                    # return = return None = raise StopIteration (either one is correct)
                    return # ends the function (no more yields) = raise StopIteration
                pair = [None, None]
    # raise StopIteration = return None = return
    raise StopIteration # to end gracefully (in my eyes at least)

if __name__=='__main__':
    #get the rss feed
    feed = urlopen("http://news.google.com/news?topic=h&output=rss")
    f = BytesIO(feed.read()) 
    feed.close()

    #create the DOM
    tree = ElementTree.parse(f)
    f.close()

    for news in top_news(tree):
        pprint(news)

    print('----------------------')

    # zip('ABCD', 'ef') --> Ae Bf
    # Returns an iterator of tuples, where the i-th tuple contains
    # the i-th element from each of the argument sequences or iterables.
    # The iterator stops when the shortest input iterable is exhausted

    # topnews as a oneliner
    topnews = lambda count=5: [(x.text, y.text) for x, y in zip
                               (tree.getiterator('title'), tree.getiterator('link')) if not
                               x.text.startswith('Top Stories')][:count]

    for news in topnews(1):
        pprint(news)        
                
