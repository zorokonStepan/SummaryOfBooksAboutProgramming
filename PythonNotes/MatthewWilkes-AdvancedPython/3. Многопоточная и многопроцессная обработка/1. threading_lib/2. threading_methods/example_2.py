import threading


class HelloWorldThread(threading.Thread):
    def run(self):
        print("Hello world!")


thread = HelloWorldThread(name="hello_world")
thread.start()
thread.join()
