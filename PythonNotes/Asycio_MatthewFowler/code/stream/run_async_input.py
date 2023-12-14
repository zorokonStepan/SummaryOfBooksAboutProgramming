import asyncio

from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.util.async_input import create_stdin_reader
from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.util.delay import delay


async def main():
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        try:
            int_delay_time = int(delay_time)
        except:
            continue
        asyncio.create_task(delay(int_delay_time))

asyncio.run(main())
