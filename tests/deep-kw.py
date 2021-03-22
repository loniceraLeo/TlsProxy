''' 关键词检测-测试 '''

import socket

plain_text = '''
GET / HTTP/1.1
Accept: */*
Host: pixiv.net
Connection: Keep-Alive

'''

if __name__ == '__main__':
    try:
        sock = socket.create_connection(('210.140.131.199', 443))
        sock.send(bytes(plain_text, 'ascii'))
        sock.settimeout(5)
        data = sock.recv(2048)
        print(data)
    except:
        raise

        