''' server-side '''

import asyncio as aio

async def process(rd: aio.StreamReader, wt: aio.StreamWriter):
    wt.write(b'123456666')
    wt.write(b'21sdwsdw')
    await wt.drain()

async def main():
    server = await aio.start_server(process,
                host='192.168.1.101', port=8082)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    aio.run(main())
