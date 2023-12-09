import threading


def hello_world():
    print("Hello world!")


thread = threading.Thread(target=hello_world, name="hello_world")
thread.start()
thread.join()
