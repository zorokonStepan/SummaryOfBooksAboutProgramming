from concurrent.futures import ThreadPoolExecutor


def hello_world():
    print("Hello world!")


with ThreadPoolExecutor() as pool:
    pool.submit(hello_world)
    