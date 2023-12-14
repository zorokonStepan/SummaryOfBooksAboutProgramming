import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor


barrier = threading.Barrier(5)


def wait_random():
    thread_id = threading.get_ident()
    to_wait = random.randint(1, 10)
    print(f"Поток {thread_id:5d}: ожидание {to_wait:2d} секунд")

    start_time = time.time()

    time.sleep(to_wait)
    i = barrier.wait()

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Поток {thread_id:5d}: возобновился в позиции {i} по истечении {elapsed:3.3f} секунд")


if __name__ == "__main__":
    with ThreadPoolExecutor() as pool:
        # Запланировать две рабочие функции
        for i in range(5):
            pool.submit(wait_random)
