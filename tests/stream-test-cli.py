import asyncio as aio

async def main():
    rd, wt = await aio.open_connection(host='210.140.131.199', 
                    port=443)
    wt.write(b'abcdefghi')
    wt.drain()
    wt.write(b'dj2dwj290kdsa')
    data = await rd.read(4096)
    await aio.sleep(2)
    print(data)

if __name__ == '__main__':
    aio.run(main())