from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

BOOKs = {
    '0132269937': {
        'title': 'Core Python Programming',
        'edition': 2,
        'year': 2006,
    },
    '0132356139': {
        'title': 'Python Web Development with Django',
        'authors': 'Jeff Forcier:Paul Bissex:Wesley Chun',
        'year': 2009,
    },
    '0137143419': {
        'title': 'Python Fundamentals',
        'year': 2009,
    },
}

books = Element('books')
for isbn, info in BOOKs.items():
    #add subelement to "books"
    book = SubElement(books, 'book')
    book.attrib["isbn"] = isbn # add attribute to subelement (like inline styling in html)

    #add data to existing dict (if it does not exist)
    info.setdefault('authors', 'Wesley Chun')
    info.setdefault('edition', 1)
    
    for key, val in info.items():
        book_data = SubElement(book, key)
        book_data.text = ', '.join(str(val).split(':'))
        # previous as oneliner-> SubElement(book, key).text = ', '.join(str(val).split(':'))

xml = tostring(books)
print('*** RAW XML ***')
print(xml)

print('\n*** PRETTY-PRINTED XML ***')
dom = parseString(xml)
print(dom.toprettyxml('    '))

print('*** FLAT STRUCTURE ***')
for elmt in books.getiterator():
    print(elmt.tag, '-', elmt.text) #attrib not showing

print('\n*** TITLES ONLY ***')
for book in books.findall('.//title'):
    print(book.text)

print('\n*** MY TITLES ONLY ***')
for book in books.findall('book'):
    for title in book.findall('title'):
        print(title.text)
