### create treads
```
    import threading
    
    
    def hello_world():
        print("Hello world!")
    
    
    thread = threading.Thread(target=hello_world, name="hello_world")
    thread.start()
    thread.join()
    
    # ####################################################################   
    
    class HelloWorldThread(threading.Thread):
        def run(self):
            print("Hello world!")
    
    thread = HelloWorldThread(name="hello_world")
    thread.start()
    thread.join()
        
    # ==================================================================================================================
    
    start() - запускает выполнение потока
    join()  - блокирует выполнение, пока поток не завершится
```

### ThreadPoolExecutor управляет используемыми потоками, позволяя ограничить число одновременно выполняемых потоков
```
    from concurrent.futures import ThreadPoolExecutor


    def calculate():
        return 2**16

    with ThreadPoolExecutor() as pool:
        task = pool.submit(calculate)
        print(task.result())  # 65536
```

### Блокировки
```
    import threading
    
    numlock = threading.Lock()
    num = 0
    def increment():
        global num
        with numlock:
            num += 1
        return None
```

### Реентерабельные блокировки
```
    numlock = threading.RLock()
```

### Условия
```
    Поток, дожидающийся данных, вызывает метод условия wait_for(...) под защитой контекстного менеджера.
    Поток, поставляющий данные, вызывает метод notify().
    
    Метод notify() пробуждает только один поток, ожидающий условия, а 
    метод notify_all() пробуждает все ожидающие потоки. 
    
    Всегда безопасно вызывать notify_all() вместо notify(), 
    но notify() экономит время, когда ожидается, что будет разблокирован только один поток.
```

### Барьеры
```
    Когда поток вызывает метод threading.Barrier(number).wait(), выполнение блокируется до тех пор, пока число ожидающих 
    потоков не сравняется с числом участников барьера.
```

### Событие
```
    threading.Event().wait() - блокировка выполнения до момента возникновения события. 
    
    threading.Event().set() - сгенерировать события. в результате будут разбужены все потоки, ожидающие этого события. 
                              Последующие обращения к wait() возвращают управление немедленно.
    
    threading.Event().clear() - событие можно также сбросить в исходное состояние.
                                тогда последующие вызовы wait() будут блокировать выполнение. 
                                
    threading.Event().is_set() - текущее состояние события 
```

### Семафор
```

```