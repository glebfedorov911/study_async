import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        # return await response.text()
        return url

async def worker(name, queue):
    async with aiohttp.ClientSession() as session:
        while True:
            url = await queue.get()
            print(f"{name} fetching {url}")
            result = await fetch(session, url)
            print(f"{name} fetched {url} with result: {result[:100]}")
            queue.task_done()

async def main():
    urls = ["http://example.com", "http://example.org", "http://example.net"]
    queue = asyncio.Queue()

    for url in urls:
        await queue.put(url)

    workers = [asyncio.create_task(worker(f"Worker-{i}", queue)) for i in range(3)] # ВЫВОДЯТСЯ ПО МЕРЕ ВЫПОЛЕНЕНИЯ, ЛУЧШЕ ИСПОЛЬЗОВАТЬ, 
                                                                                    # КОГДА НУЖНА ДИНАМИКА И КОНТРОЛЬ НАД КОЛИЧЕСТВОМ ЗАДАЧ

    await queue.join()

    for w in workers:
        w.cancel()

asyncio.run(main())