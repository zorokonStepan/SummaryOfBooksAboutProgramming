import random
import time
import threading

from concurrent.futures import ThreadPoolExecutor


event = threading.Event()


def wait_random(master):
    thread_id = threading.get_ident()
    to_wait = random.randint(1, 10)
    print(f"Поток {thread_id:5d}: ожидание {to_wait:2d} секунд (Главный: {master})")

    start_time = time.time()

    time.sleep(to_wait)
    if master:
        event.set()
    else:
        event.wait()

    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Поток {thread_id:5d}: возобновился по истечении {elapsed:3.3f} секунд")


if __name__ == "__main__":
    with ThreadPoolExecutor() as pool:
        # Запланировать две рабочие функции
        for i in range(4):
            pool.submit(wait_random, False)
        pool.submit(wait_random, True)
