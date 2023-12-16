import multiprocessing


def worker():
    print('Worker')


if __name__ == '__main__':
    for _ in range(5):
        multiprocessing.Process(target=worker).start()
