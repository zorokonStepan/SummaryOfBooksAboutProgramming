import time
import threading

from concurrent.futures import ThreadPoolExecutor


data = []
results = []
running = True
data_available = threading.Condition()
work_complete = threading.Condition()


def has_data():
    return bool(data)


def num_complete(n):
    """ Вернуть функцию, которая проверяет, что в списке results находится n элементов """
    def finished():
        return len(results) >= n
    return finished


def calculate():
    while running:
        with data_available:
            # Захватить блокировку data_available lock и ждать условия has_data
            print("Ожидание данных")
            data_available.wait_for(has_data)
            time.sleep(1)
            i = data.pop()

            with work_complete:
                if i % 2:
                    results.append(1)
                else:
                    results.append(0)

                # Захватить блокировку work_complete и пробудить ожидающих
                work_complete.notify_all()


if __name__ == "__main__":
    with ThreadPoolExecutor() as pool:
        # Запланировать две рабочие функции
        workers = [pool.submit(calculate), pool.submit(calculate)]

        for i in range(200):
            with data_available:
                data.append(i)
                # После добавления каждого элемента данных уведомлять data_available
                data_available.notify()
        print("Помещено 200 элементов")

        with work_complete:
            # С помощью условия work_complete ждать, когда будет обработано по крайней мере 5 элементов
            work_complete.wait_for(num_complete(5))

        for worker in workers:
            # Установить разделяемую переменную, сигнализирующую потокам, что пора заканчивать
            running = False

        print("\nОстанавливаются рабочие потоки")

    print(f"Обработано элементов: {len(results)}")
