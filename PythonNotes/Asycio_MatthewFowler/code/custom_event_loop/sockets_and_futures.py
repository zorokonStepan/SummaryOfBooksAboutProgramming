import functools
import selectors
import socket
from selectors import BaseSelector

from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.custom_event_loop.custom_future import CustomFuture


def accept_connection(future: CustomFuture, connection: socket):
    print(f'Получен запрос на подключение от {connection}!')
    future.set_result(connection)


async def sock_accept(sel: BaseSelector, sock) -> socket:
    print('Регистрируется сокет для прослушивания подключений')
    future = CustomFuture()
    sel.register(sock, selectors.EVENT_READ, functools.partial(accept_connection, future))
    print('Прослушиваю запросы на подключение...')
    connection: socket = await future
    return connection


async def main(sel: BaseSelector):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('127.0.0.1', 8000))
    sock.listen()
    sock.setblocking(False)

    print('Ожидаю подключения к сокету!')
    connection = await sock_accept(sel, sock)
    print(f'Получено подключение {connection}!')


selector = selectors.DefaultSelector()
coro = main(selector)


while True:
    try:
        state = coro.send(None)
        events = selector.select()

        for key, mask in events:
            print('Обрабатываются события селектора...')
            callback = key.data
            callback(key.fileobj)

    except StopIteration as si:
        print('Приложение завершилось!')
        break
