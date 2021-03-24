#! python3
''' Author: github.com/loniceraLeo
'''

'''
    TODO: random padding length
    TODO: hash algorithms switch
'''

import random
import sys
from hashlib import blake2b, blake2s

def nop(*args, **kwargs):
    pass

def check_python_version(major, minor, micro) -> bool:
    if sys.version_info < (major, minor, micro):
        return False
    return True

def mask(payload: bytes, pwd: bytes, first=0) -> tuple:
    ''' do mask in xor operation.
        the function ensures an ordered mask-unmask behavior. '''
    data = bytearray(payload)
    for i in range(len(data)):
        data[i] = data[i] ^ pwd[(i+first)%len(pwd)]
    last = (len(data)+first) % len(pwd)
    return (data, last)

def hashed_key(key: bytes, size=32) -> bytes:
    ''' check https://www.blake2.net/ for more information '''
    return blake2b(key, digest_size=size).digest()

def is_valid_address(hostname: str, port: int) -> bool:
    if port != 80 and port != 443:
        return False
    try:
        for i in range(len(hostname)):
            ascii_num = ord(hostname[i])
            if hostname[i] == '.' or hostname[i] == '-' or \
                ascii_num in list(range(48, 58)) or \
                    ascii_num in list(range(65, 91)) or \
                        ascii_num in list(range(97, 123)):
                continue
            else:
                return False
    except:
        return False
    return True

def padding(addr: bytes, padding_length: int) -> bytes:
    addr_length = len(addr)
    if addr_length >= padding_length:
        raise ValueError('padding length over limitation')
    payload = bytearray(b'')
    payload.append(addr_length)
    payload.extend(addr)
    pads = random.randbytes(padding_length-addr_length-1)
    payload.extend(pads)
    return payload

def is_valid_address_test(host, port):
    print(is_valid_address(host, port))

if __name__ == '__main__':
    nop()