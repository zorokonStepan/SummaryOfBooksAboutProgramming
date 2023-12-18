import asyncio


@asyncio.coroutine
def outer():
    print('in outer')
    print('waiting for result_1')
    result_1 = yield from phase_1()
    print('waiting for result_2')
    result_2 = yield from phase_2(result_1)
    return result_1, result_2


@asyncio.coroutine
def phase_1():
    print('in phase_1')
    return 'result_1'


@asyncio.coroutine
def phase_2(arg):
    print('in phase_2')
    return 'result_2 derived from {)'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('return value: {!r}'.format(return_value))
finally:
    event_loop.close()
