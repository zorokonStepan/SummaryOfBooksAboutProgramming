import time
import multiprocessing


def stage_1(cond):
    """Выполнить первый этап работы, а затем уведомить stage_2 для продолжения."""
    name = multiprocessing.current_process().name
    print('Starting', name)

    with cond:
        print('{} done and ready for stage 2'.format(name))
        cond.notify_all()


def stage_2(cond):
    """Дождаться условия, сообщающего, что stage_1 завершен."""
    name = multiprocessing.current_process().name
    print('Starting', name)

    with cond:
        cond.wait()
        print('{} running'.format(name))


if __name__ == '__main__':
    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(name='s1', target=stage_1, args=(condition,))
    s2_clients = [
        multiprocessing.Process(name='stage_2[{}]'.format(i), target=stage_2, args=(condition,)) for i in range(1, 3)
    ]

    for c in s2_clients:
        c.start()
        time.sleep(1)
        s1.start()
        s1.join()

    for c in s2_clients:
        c.join()
