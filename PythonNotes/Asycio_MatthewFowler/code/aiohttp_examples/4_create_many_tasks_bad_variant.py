import asyncio

from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.util.async_timer import async_timed
from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.util.delay import delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

asyncio.run(main())
