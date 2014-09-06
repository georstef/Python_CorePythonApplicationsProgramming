'''
 jeff knupp's - NoSQL database
'''
import socket

HOST = ''
PORT = 5555
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
STATS = {
    'PUT': {'success': 0, 'errors': 0},
    'GET': {'success': 0, 'errors': 0},
    'GETLIST': {'success': 0, 'errors': 0},
    'PUTLIST': {'success': 0, 'errors': 0},
    'INCREMENT': {'success': 0, 'errors': 0},
    'APPEND': {'success': 0, 'errors': 0},
    'DELETE': {'success': 0, 'errors': 0},
    'STATS': {'success': 0, 'errors': 0},
}


def parse_message(data):
    """"
    Return a tuple containing the command, the key, and (optionally) the value cast to the appropriate type.
    """
    command, key, value, value_type = data.strip().split(';')
    if value_type:
        if value_type == 'LIST':
            value = value.split(',')
        elif value_type == 'INT':
            value = int(value)
        else:
            value = str(value)
    else:
        value = None
    return command, key, value


def update_stats(command, success):
    if success:
        STATS[command]['success'] += 1
    else:
        STATS[command]['errors'] += 1


def nosql_put(key, value):
    DATA[key] = value
    return True, 'Key [{0}] set to [{1}]'.format(key, value)


def nosql_get(key):
    if key not in DATA:
        return False, 'ERROR Key [{0}] not found'.format(key)
    else:
        return True, DATA[key]


def nosql_getlist(key):
    return_value = exists, value = nosql_get(key)
    if not exists:
        return return_value
    elif not isinstance(value, list):
        return False, 'ERROR Key [{0}] not a list but [{1}]'.format(key, value)
    else:
        return return_value


def nosql_putlist(key, value):
        return nosql_put(key, value)


def nosql_increment(key):
    return_value = exists, value = nosql_get(key)
    if not exists:
        return return_value
    elif not isinstance(value, int):
        return False, 'ERROR Key [{0}] not an integer but [{1}]'.format(key, value)
    else:
        DATA[key] = value + 1
        return True, 'Key [{}] incremented'.format(key)


def nosql_append(key, value):
    return_value = exists, list_value = nosql_getlist(key)
    if not exists:
        return return_value
    else:
        DATA[key].append = value
        return True, 'Key [{0}] had value [{1}] appended'.format(key, value)


def nosql_delete(key):
    if key not in DATA:
        return False, 'ERROR Key [{0}] not found'.format(key)
    else:
        del DATA[key]
        return True,  'Key [{0}] deleted'.format(key)


def nosql_stats():
    return True, str(STATS)


COMMAND_HANDLERS = {
    'PUT': nosql_put,
    'GET': nosql_get,
    'GETLIST': nosql_getlist,
    'PUTLIST': nosql_putlist,
    'INCREMENT': nosql_increment,
    'APPEND': nosql_append,
    'DELETE': nosql_delete,
    'STATS': nosql_stats,
}

DATA = {}


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    while True:
        connection, address = server_socket.accept()
        print('New connection from [{0}]'.format(address))
        data = connection.recv(4096).decode('utf-8')
        command, key, value = parse_message(data)
        if command == 'STATS':
            response = COMMAND_HANDLERS[command]()
        elif command in ('GET', 'GETLIST', 'INCREMENT', 'DELETE'):
            response = COMMAND_HANDLERS[command](key)
        elif command in ('PUT', 'PUTLIST', 'APPEND'):
            response = COMMAND_HANDLERS[command](key, value)
        else:
            response = False, 'Unknown command [{}]'.format(command)

        update_stats(command, response[0])
        connection.sendall(bytes('{};{}'.format(response[0], response[1]), 'utf-8'))
        connection.close()
    server_socket.close()


if __name__ == '__main__':
    main()
