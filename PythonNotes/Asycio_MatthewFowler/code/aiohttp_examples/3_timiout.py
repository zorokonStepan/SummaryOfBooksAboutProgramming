import asyncio
from aiohttp import ClientSession, ClientTimeout


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = ClientTimeout(total=0.01)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    session_timeout = ClientTimeout(total=1, connect=0.1)
    async with ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://example.com')

asyncio.run(main())
