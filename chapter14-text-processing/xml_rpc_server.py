# import SimpleXMLRPCServer
from  xmlrpc.server import SimpleXMLRPCServer
import csv
import operator
import time
import codecs
from urllib.request import urlopen
# import twitter_app # twapi.py from chapter 13

server = SimpleXMLRPCServer(("localhost", 8888))

# introspection functions allow clients to query the server
# to determine its capabilities
# They assist the client in establishing:
# 1. what methods the server supports (system.listMethods)
# 2. how it can call a specific RPC (system.methodSignature)
# 3. whether there is any documentation (system.methodHelp)
server.register_introspection_functions() 

FUNCs = ('add', 'sub', 'mul', 'floordiv', 'mod')

# registering functions
for f in FUNCs:
    server.register_function(getattr(operator, f)) # example of getattr
server.register_function(pow) # register the function

class SomeOtherFunctions(object):
    def now_int(self):
        return time.time()

    def now_str(self):
        return time.ctime()

    def timestamp(self, s):
        return '[%s] %s' % (time.ctime(), s)

    def stock(self, s):
        url = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=l1c1p2d1t1'
        u = urlopen(url % s)
        reader = csv.reader(codecs.iterdecode(u, 'utf-8')) # in python v3.x 'u' returns bytes that needs decoding
        res = reader.__next__() # the first/next item of the iterable
        u.close() # this closes 'u' and 'reader'
        return res
    
    def forex(self, s='usd', t='eur'):
        url = 'http://quote.yahoo.com/d/quotes.csv?s=%s%s=X&f=nl1d1t1'
        u = urlopen(url % (s, t))
        reader = csv.reader(codecs.iterdecode(u, 'utf-8')) # in python v3.x 'u' returns bytes that needs decoding
        res = reader.__next__()  # the first/next item of the iterable
        u.close() # this closes 'u' and 'reader'
        return res

    def status(self):
        return 'Not Implemented'
    def tweet(self, s):
        return 'Not Implemented'
    '''
    def status(self):
        t = twitter_app.Twitter('twython')
        res = t.verify_credentials()
        status = twitter_app.ResultsWrapper(res.status)
        return status.text

    def tweet(self, s):
        t = twitter_app.Twitter('twython')
        res = t.update_status(s)
        return res.created_at
    '''

# registering instance of an object
server.register_instance(SomeOtherFunctions())

try:
    print('Welcome to XML-RPC PotpourriServ v0.1\n(Use ^C to exit)')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
