import time
import logging
import threading


def consumer(cond):
    """Дождаться наступления условия и затем использовать ресурс."""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')


def producer(cond):
    """Настроить ресурс для использования потребителем."""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notify_all()


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-2s) %(message)s')

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()
