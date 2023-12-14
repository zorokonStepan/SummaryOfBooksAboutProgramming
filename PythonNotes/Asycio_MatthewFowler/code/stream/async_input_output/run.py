import asyncio
import os
import sys
import tty
from collections import deque

from message_store import MessageStore
from util import (move_to_bottom_of_screen, save_cursor_position, move_to_top_of_screen, restore_cursor_position,
                  delete_line)
from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.util.async_input import create_stdin_reader
from async_read import read_line


async def sleep(delay: int, message_store: MessageStore):
    await message_store.append(f'Начало задержки {delay}')
    await asyncio.sleep(delay)
    await message_store.append(f'Конец задержки {delay}')


async def main():
    tty.setcbreak(sys.stdin)
    os.system('clear')
    rows = move_to_bottom_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(redraw_output, rows - 1)

    stdin_reader = await create_stdin_reader()

    while True:
        line = await read_line(stdin_reader)
        delay_time = int(line)
        asyncio.create_task(sleep(delay_time, messages))


asyncio.run(main())
