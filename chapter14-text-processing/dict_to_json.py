# exact copy of the example

import json
import pprint

BOOKs = {
    '013xxx37': {
        'title': 'Core Python Progr.',
        'edition': 2,
        'year': 2007
        },
    '013xxx39': {
        'title': 'Python Web Dev.',
        'authors': ['Jeff', 'Paul', 'Wesley'],
        'year': 2009
        },
    '013xxx19': {
        'title': 'Python Fundamentals',
        'year': 2009
        }
    }

if __name__ == '__main__':
    print(BOOKs)
    print('---------------------')
    pprint.pprint(BOOKs)
    print('---------------------')
    print(json.dumps(BOOKs))
    print('---------------------')
    print(json.dumps(BOOKs, indent=4))
