import asyncio
from aiohttp import ClientSession

from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.util.async_timer import async_timed
from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.util.fetch_status import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
