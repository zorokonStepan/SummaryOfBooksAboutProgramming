import asyncio
from asyncio import StreamReader
import sys


async def create_stdin_reader() -> StreamReader:
    """
    not worked from Windows
    """
    stream_reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(stream_reader)
    loop = asyncio.get_running_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    return stream_reader
