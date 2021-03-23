#! python3
''' Author: github.com/loniceraLeo
'''

import sys

def nop(*args, **kwargs):
    pass

dic = {
    '-c': 'config',
    '-s': 'server',
    '-p': 'port',
    '-'
    '-r': 'recursion_mode',
}

def parse():
    argv = sys.argv
    print(argv)

if __name__ == '__main__':
    parse()