# exact copy of the example
# gets some stock data from "finance.yahoo.com"

from time import ctime
from urllib.request import urlopen
import codecs
import csv

TICKs = ('yhoo', 'dell', 'cost', 'adbe', 'intc')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'

print('\nPrices quoted as of: %s\n' % ctime())
print('TICKER', 'PRICE', 'CHANGE', '%AGE')
print('------', '-----', '------', '----')

# urlopen returns a file-like object
u = urlopen(URL % ','.join(TICKs))

reader = csv.reader(codecs.iterdecode(u, 'utf-8')) # python v3.x returns bytes that needs decoding
for tick, price, chg, per in reader:
    print(tick, '%.2f' % float(price), chg, per.rstrip())#.rstrip() <- for suppressing newline characters

u.close()

