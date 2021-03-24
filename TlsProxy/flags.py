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
            if dic[item] == 'r':
                try:
                    conf = config.search_recursively(os.getcwd(),
                            argv[index+1])
                except:
                    raise
                print(1)
                return conf
        except KeyError:
            continue

if __name__ == '__main__':
    parse()