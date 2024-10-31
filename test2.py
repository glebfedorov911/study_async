import aiohttp
import asyncio


async def fetch(session: aiohttp.ClientSession, url: str, delay: int):
    await asyncio.sleep(delay=delay)
    async with session.get(url) as response:
        return await response.text()

async def worker(queue: asyncio.Queue):
    async with aiohttp.ClientSession() as session:
        while True:
            url, delay = await queue.get()
            print(f"Делаем запрос на {url}, ожидание...")
            await fetch(session=session, url=url, delay=delay)
            print(f"Данные полученные с сайта {url}, задержка: {delay}")
            queue.task_done()

async def main(data):
    queue = asyncio.Queue()

    for url, delay in data:
        await queue.put((url, delay))

    workers = [asyncio.create_task(worker(queue=queue)) for _ in range(3)]
    
    await queue.join()

    for wrk in workers:
        wrk.cancel()
    
if __name__ == "__main__":
    data = [
        ("http://example.com", 8),
        ("http://example.org", 3),
        ("http://example.net", 1),
    ] * 2

    asyncio.run(main(data))