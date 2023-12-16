import threading


def worker(num):
    print('Worker: %s' % num)


for i in range(5):
    threading.Thread(target=worker, args=(i,)).start()
