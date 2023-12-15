import threading


def worker():
    print('Worker')


for _ in range(5):
    threading.Thread(target=worker).start()
