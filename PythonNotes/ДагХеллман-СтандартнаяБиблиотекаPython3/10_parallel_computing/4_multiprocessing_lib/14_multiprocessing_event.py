import time
import multiprocessing


def wait_for_event(event):
    """Дождаться события, прежде чем делать что-либо."""
    print('wait_for_event: starting')
    event.wait()
    print('wait_for_event: event.is_set()->', event.is_set())


def wait_for_event_timeout(event, t):
    """Подождать t секунд и затем завершиться по тайм-ауту."""
    print('wait_for_event_timeout: starting')
    event.wait(t)
    print('wait_for_event_timeout: event.is_set()->', event.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name='block', target=wait_for_event, args=(e,))
    w1.start()
    w2 = multiprocessing.Process(name='nonblock', target=wait_for_event_timeout, args=(e, 2))
    w2.start()
    print('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('main: event is set')
