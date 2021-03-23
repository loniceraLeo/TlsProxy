#! python3
''' Author: github.com/loniceraleo
    server-side of TLS-Proxy 
'''

import asyncio
import ssl

from TlsProxy import config
from .config import SERVER_SIDE
from .utils import *

def nop(*args, **kwargs):
    pass

async def process(rd: asyncio.StreamReader, wt: asyncio.StreamWriter):
    ''' we shouldn't use ssl mode because the http proxy
    transports the encrypted data in the tunnel. 
    '''
    data = await rd.read(256)
    raw_adr, _ = mask(data, new_key)
    adr = extract_address(raw_adr)
    host, port = adr.split(':')[0], \
                int(adr.split(':')[1], 10)
    if not is_valid_address(host, port):
        return
    try:
        rmt_rd, rmt_wt = await asyncio.open_connection(
            host=host, port=port) 
    except:
        wt.close()
        return 

    await asyncio.gather(stream_copy(rd, rmt_wt), 
                        stream_copy(rmt_rd, wt))        

async def stream_copy(reader: asyncio.StreamReader, 
    writer: asyncio.StreamWriter, toggle=False):
    first = 0
    try:
        while True:
            data, first = mask(await reader.read(8192), \
                        new_key, first)
            if toggle:
                print(data[:30])
            if data == b'':
                if writer:
                    writer.close()
                return
            writer.write(data)
            await writer.drain()
    except:
        if writer:
            writer.close()
        return

def extract_address(raw_data: bytes) -> str:
    length = raw_data[0]
    raw_address = raw_data[1:1+length]
    address = str(bytes(raw_address))[2:-1]
    return address

async def main():
    server = await asyncio.start_server(process, 
    host=conf['server'], port=conf['port'],
    ssl=ctx, ssl_handshake_timeout=30)

    '''XXX no event-loop exception warning.
    it will be optional in the future '''
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(nop)
    no_check(loop)

    async with server:
        await server.serve_forever()

def init():
    if not check_python_version(3, 7, 0):
        ''' the asyncio api needs python3.7+ '''
        raise ValueError('python version not support')

def handle_exception(loop, context):
    ''' TODO: implement a user-specified exception handler '''
    print(context)

def entry():
    global conf, new_key, ctx

    try:
        conf = config.get_config(SERVER_SIDE)
        new_key = hashed_key(conf['password'])
        ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ctx.load_cert_chain(conf['certificate'], conf['private-key'])

        asyncio.run(main())
    except KeyboardInterrupt:
        exit(1)

def no_check(loop: asyncio.AbstractEventLoop):
    '''XXX not safe
    '''
    loop._check_closed = nop

if __name__ == '__main__':
    nop()
