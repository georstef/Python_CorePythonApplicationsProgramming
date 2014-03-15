from math import pi
from xmlrpc.client import ServerProxy

server = ServerProxy('http://localhost:8888') # connect to the XML-RPC server

print('Current time in seconds after epoch:', server.now_int())
print('Current time as a string:', server.now_str())
print('Area of circle of radius 5:', server.mul(pi, server.pow(5, 2)))

stock = server.stock('goog')
print('Latest Google stock price: %s (%s / %s) as of %s at %s' % tuple(stock))

forex = server.forex()
print('Latest foreign exchange rate from %s: %s as of %s at %s' % tuple(forex))

forex = server.forex('eur', 'usd')
print('Latest foreign exchange rate from %s: %s as of %s at %s' % tuple(forex))

print('Latest Twitter status:', server.status())
print('Posted tweet at:', server.tweet('Latest GOOG stock price is %s' % stock))

# calling the introspection functions
print(server.system.listMethods())
print(server.system.methodSignature('system.methodHelp'))
print(server.system.methodHelp('floordiv'))

