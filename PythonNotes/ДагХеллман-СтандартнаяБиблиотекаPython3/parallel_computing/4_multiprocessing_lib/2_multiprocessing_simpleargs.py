import multiprocessing


def worker(num):
    print('Worker:', num)


if __name__ == '__main__':
    for i in range(5):
        multiprocessing.Process(target=worker, args=(i,)).start()
