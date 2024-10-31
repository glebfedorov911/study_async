import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        # return await response.text()
        return url

async def main():
    urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls] 
        results = await asyncio.gather(*tasks)
    print("All results fetched:", results) #ВЫВОДИТСЯ РЕЗУЛЬТАТ ТОГДА, КОГДА ВЫПОЛНИЛИСЬ ВСЕ (ЛУЧШЕ ИСПОЛЬЗОВАТЬ С ФИКСИРОВАННЫМ И МАЛЫМ КОЛИЧЕСТВОМ ЗАДАЧ)

asyncio.run(main())
