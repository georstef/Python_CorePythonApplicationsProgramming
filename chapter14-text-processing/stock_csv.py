# not the exact copy of the example (some changes for python v3.0)
# gets some stock data from "finance.yahoo.com"

from time import ctime
from urllib.request import urlopen
import codecs
import csv
from io import TextIOWrapper

TICKs = ('yhoo', 'dell', 'cost', 'adbe', 'intc')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'

print('\nPrices quoted as of: %s\n' % ctime())
print('TICKER', 'PRICE', 'CHANGE', '%AGE')
print('------', '-----', '------', '----')

# urlopen returns a file-like object
u = urlopen(URL % ','.join(TICKs))

#1. convert a file like object from bytes to string
# reader = csv.reader(codecs.iterdecode(u, 'utf-8')) # in python v3.x 'u' returns bytes that needs decoding

#2. convert a file like object from bytes to string
f = TextIOWrapper(u, encoding='utf-8') # in python v3.x 'u' returns bytes that needs decoding
reader = csv.reader(f) 
print(reader.__next__())
# at this point reader is already converted to string (one way or the other)
for tick, price, chg, per in reader:
    print(tick, '%.2f' % float(price), chg, per.rstrip())#.rstrip() <- for suppressing newline characters
u.close()


# for only 1 value
u = urlopen('http://quote.yahoo.com/d/quotes.csv?s=goog&f=l1c1p2d1t1')
reader = csv.reader(codecs.iterdecode(u, 'utf-8')) # in python v3.x 'u' returns bytes that needs decoding
res = reader.__next__()
u.close()
print('Latest Google stock price: %s (%s / %s) as of %s at %s' % tuple(res))
