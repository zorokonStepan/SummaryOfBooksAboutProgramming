import time
import multiprocessing


def worker():
    process_name = multiprocessing.current_process().name
    print(process_name, 'Starting')
    time.sleep(2)
    print(process_name, 'Exiting')


def my_service():
    process_name = multiprocessing.current_process().name
    print(process_name, 'Starting')
    time.sleep(3)
    print(process_name, 'Exiting')


if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service)
    worker_1 = multiprocessing.Process(name='worker 1', target=worker)
    worker_2 = multiprocessing.Process(target=worker)

    worker_1.start()
    worker_2.start()
    service.start()
