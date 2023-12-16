import time
import logging
import threading


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

daemon_1 = threading.Thread(name='daemon_1', target=daemon, daemon=True)
no_daemon = threading.Thread(name='non-daemon', target=non_daemon)
daemon_2 = threading.Thread(name='daemon_2', target=daemon)
daemon_2.daemon = True

daemon_2.start()
daemon_1.start()
no_daemon.start()

daemon_1.join(0.1)
print('d.isAlive()', daemon_1.is_alive())
no_daemon.join()

daemon_2.join()
