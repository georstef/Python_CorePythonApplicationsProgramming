#when this file is in a cgi-bin folder it get executed
#that means that the comment lines will be invisible
#if they are visible then you are seeing this script as static text
print('Content-type: text/html\n')

print('<HTML><HEAD><TITLE>Python Sample CGI</TITLE></HEAD>')
print('<BODY>')
print('<H1>This is a header</H1>')

print('<p>') #this is a comment
print('See this is just like most other HTML')
print('<br>')
print('</BODY>')
		
