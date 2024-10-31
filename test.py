import asyncio
import aiohttp


async def fetch_example_com(queue):
    await asyncio.sleep(1) 
    async with aiohttp.ClientSession() as session:
        async with session.get("http://example.com") as response:
            result = f"Fetched data from example.com with status {response.status}"
            await queue.put(result)

async def fetch_example_org(queue):
    await asyncio.sleep(2) 
    async with aiohttp.ClientSession() as session:
        async with session.get("http://example.org") as response:
            result = f"Fetched data from example.org with status {response.status}"
            await queue.put(result)

async def fetch_example_net(queue):
    await asyncio.sleep(5) 
    async with aiohttp.ClientSession() as session:
        async with session.get("http://example.net") as response:
            result = f"Fetched data from example.net with status {response.status}"
            await queue.put(result)

async def main():
    queue = asyncio.Queue()

    tasks = [
        fetch_example_com(queue),
        fetch_example_org(queue),
        fetch_example_net(queue)
    ]

    await asyncio.gather(*tasks)

    while not queue.empty():
        print(await queue.get())

asyncio.run(main())
