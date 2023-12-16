import time
import threading


def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().name, 'Exiting')


def my_service():
    print(threading.current_thread().name, 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().name, 'Exiting')


t = threading.Thread(name='my__service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # использовать имя по умолчанию

w.start()
w2.start()
t.start()
