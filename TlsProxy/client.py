#! python3
''' Author: github.com/loniceraleo
    client-side of TLS-Proxy 
    warnning: python3.7+ needed '''

import asyncio
from os import write
import socket
import ssl

from TlsProxy import config
from TlsProxy.config import CLIENT_SIDE
from TlsProxy.utils import *

def nop(*args, **kwargs):
    pass

async def process_stream(rd: asyncio.StreamReader, 
        wt: asyncio.StreamWriter):
    data = await rd.read(4096)
    raw_addr = data.split(b' ')[1]
    padded_addr = padding(raw_addr, conf['padding-length'])
    addr, _ = mask(padded_addr, new_key)

    print(raw_addr)
    try:
        rmt_rd, rmt_wt = await asyncio.open_connection(
            host=conf['server'], port=conf['port'],
            ssl=ctx, ssl_handshake_timeout=30)
    except:
        wt.close()
        return

    rmt_wt.write(addr)
    await rmt_wt.drain()

    wt.write(b'HTTP/1.1 200 Connection Established\r\n\r\n')
    await wt.drain()
    await asyncio.gather(stream_copy(rd, rmt_wt), 
                            stream_copy(rmt_rd, wt),
                            return_exceptions=True)

async def stream_copy(reader: asyncio.StreamReader, 
    writer: asyncio.StreamWriter, toggle=False):
    first = 0
    try:
        while True:
            data, first = mask(await reader.read(8192), \
                    new_key, first)
            if data == b'':
                if writer is not None:
                    writer.close()
                return
            writer.write(data)
            await writer.drain()
    except:
        try:
            if writer is not None:
                writer.close()
            return
        except:
            return

async def check_valid(reader: asyncio.StreamReader) -> bool:
    ''' the server side create a recipe 
        Deprecated: useless function.
    '''
    token = await reader.read(4096)
    token, _ = mask(token, new_key)
    if token == b'Connection Established':
        return True
    return False

def destory_conns(conns: list):
    for writer in conns:
        del writer.transport

async def main():
    global server

    server = await asyncio.start_server(process_stream,
        host=conf['local_host'], port=conf['local_port'])
    ''' TODO: use logging module in the future '''
    print('{0}:{1} is on listening...'.format(
        conf['local_host'], conf['local_port']
    ))

    ''' no event-loop exception warning.
        it will be optional in the future '''

    loop = asyncio.get_running_loop()
    loop.set_exception_handler(nop)
    no_check(loop)

    async with server:
            await server.serve_forever()

def entry():
    global new_key, ctx, conf, rmt_conns

    try:
        conf = config.get_config(CLIENT_SIDE)
        new_key = hashed_key(conf['password'].encode())
        ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ctx.check_hostname = False
        rmt_conns = []
        
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')

def no_check(loop: asyncio.AbstractEventLoop):
    '''XXX not safe!
    we override a private method of event loop to avoid raising exception
    consider constructing a sub-class of event-Loop?
    '''
    loop._check_closed = nop

if __name__ == '__main__':
    entry()