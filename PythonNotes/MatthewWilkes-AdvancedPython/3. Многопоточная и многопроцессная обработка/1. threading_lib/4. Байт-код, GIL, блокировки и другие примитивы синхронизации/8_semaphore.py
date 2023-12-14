import random
import time
import threading

from concurrent.futures import ThreadPoolExecutor


semaphore = threading.Semaphore(3)


def wait_random():
    thread_id = threading.get_ident()
    to_wait = random.randint(1, 10)

    with semaphore:
        print(f"Поток {thread_id:5d}: ожидание {to_wait:2d} секунд")
        start_time = time.time()

        time.sleep(to_wait)
        end_time = time.time()
        elapsed = end_time - start_time

        print(f"Поток {thread_id:5d}: возобновился по истечении {elapsed:3.3f} секунд")


if __name__ == "__main__":
    with ThreadPoolExecutor() as pool:
        # Запланировать две рабочие функции
        for i in range(5):
            pool.submit(wait_random)
