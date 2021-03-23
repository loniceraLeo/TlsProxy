#! python3
''' Author: github.com/loniceraLeo
'''

import os
import json
import ssl
from os import system as sys_call

SERVER_SIDE = 0x0
CLIENT_SIDE = 0x1

def nop(*args, **kwargs):
    pass

def get_config(*args) -> dict:
    files = os.listdir()
    for name in files:
        if name == 'config.json':
            config = read_config()
            if not 'private_key' in config and args[0] == SERVER_SIDE:
                raise ValueError('not server config')
            return config
    return create_config(args[0])

def set_config():
    ''' reserve this method for future implementation
    '''
    pass

def read_config() -> dict:
    with open('./config.json', 'r') as f:
        marshalled_data = f.read()
        config = json.loads(marshalled_data)
    return config

def create_config(side: int) -> dict:
    ''' creates a new config.json file and save it in the
        current dictionary 
    '''
    config = {}
    config['server']          = input('server: ')
    config['port']            = input('port: ')
    config['password']        = input('password: ')
    if side == CLIENT_SIDE:
        config['local_host']  = '127.0.0.1'
        config['local_port']  = input('local_port: ')
    if side == SERVER_SIDE:
        config['certificate'] = input('certificate: ')
        config['private-key'] = input('private-key: ')
        generate_key_cert(config['private-key'], config['certificate'])
    config['hash-algorithm']  = 'blake2b'
    config['padding-length']  = 256

    jsoned_config = json.dumps(obj=config, indent=4)

    with open('./config.json', 'w') as f:
        f.write(jsoned_config)

    return config

def generate_key_cert(key_file, cert_file, *, format: str=None) -> None:
    ''' if current os support, use openssl.
        if argument format is not specified, create a default
        private key and use it to generate a self-signed certificate.
        it is recommended to use default format 
    '''
    files = os.listdir()
    if key_file in files or cert_file in files:
        return 
    try:
        o_v = ssl.OPENSSL_VERSION_INFO
    except:
        raise ValueError('openssl not support')
    default_key_format = {
        'cipher': 'aes256',
        'length': 2048,
        'no-pharse': True   # generate a private without pass pharse
    }
    default_cert_format = {
        'last-time': 3650  # maximum
    }
    if format:  
        ''' TODO: implement user-specified private key and certificate '''
        pass
    else:
        sys_call('openssl genrsa -{0} -out {1} {2}'.format(\
            default_key_format['cipher'], key_file, \
            default_key_format['length']))
        # no pass pharse:
        sys_call('openssl rsa -in {0} -out {0}'.format(\
            key_file))
        sys_call('openssl req -new -x509 -days {0} -key {1} -out {2}'.\
            format(default_cert_format['last-time'],
            key_file, cert_file))

def search_recursively(dir: str) -> str:
    files = os.listdir(dir)
    for file_name in files:
        if file_name == 'config.json':
            with open(dir+'/'+file_name) as f:
                data = f.read()
                return data
        if is_dir(file_name):
            return search_recursively(dir+'/'+file_name)
    return None

def is_dir(filename: str) -> bool:
    if not '.' in filename:
        return True
    return False

if __name__ == '__main__':
    #generate_key_cert('abc.key', 'abc.crt')
    nop()