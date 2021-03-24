#! python3
''' Author: github.com/loniceraLeo
'''

import os
import sys

from TlsProxy import config

def nop(*args, **kwargs):
    pass

dic = {
    '-c': 'c', 
    '-g': 'g',
    '-r': 'r',
    '-h': 'h'
}

def parse() -> any:
    argv = sys.argv
    for index, item in enumerate(argv):
        try:
            if dic[item] == 'c':
                try:
                    conf = config.read_config(argv[index+1])
                except:
                    return None
                return conf
            if dic[item] == 'g':
                try:
                    config.generate_key_cert(argv[index+1], 
                        argv[index+2])
                except:
                    return None
                exit()
            if dic[item] == 'r':
                try:
                    conf = config.search_recursively(os.getcwd(),
                            argv[index+1])
                except:
                    return
                if conf == None:
                    print('file not found')
                    exit()
                return conf
            if dic[item] == 'h':
                help_inf()
                exit()

        except KeyError:
            continue
    return None

def help_inf():
    print('''
Usage of TlsProxy:
    tpclient/tpserver [flag] [filename] ...
        
    flag:
        -c filename : use filename as config file
        -g filename1 filename2 : generate a key and a self-signed 
        certificate. Respectively named filename1 and filename2
        -r filename : search filename in current directory recursively
        -h : help information
            
    ''')

if __name__ == '__main__':
    help_inf()