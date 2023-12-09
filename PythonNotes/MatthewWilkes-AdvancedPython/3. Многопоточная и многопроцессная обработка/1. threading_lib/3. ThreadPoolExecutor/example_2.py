from concurrent.futures import ThreadPoolExecutor


def calculate():
    return 2 ** 16


with ThreadPoolExecutor() as pool:
    task = pool.submit(calculate)
    print(task.result())  # 65536
    