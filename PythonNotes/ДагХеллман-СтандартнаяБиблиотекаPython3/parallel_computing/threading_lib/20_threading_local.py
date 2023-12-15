import random
import threading
import logging


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

local_data = threading.local()
show_value(local_data)

local_data.value = 1000
show_value(local_data)

for _ in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
