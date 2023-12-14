from ProgrammingLanguages.Python.book_abstracts.Asycio_MatthewFowler.code.custom_event_loop.custom_future import CustomFuture


future = CustomFuture()
i = 0


while True:
    try:
        print('Проверяется будущий объект...')
        gen = future.__await__()
        gen.send(None)
        print('Будущий объект не готов...')
        if i == 2:
            print('Устанавливается значение будущего объекта...')
            future.set_result('Готово!')
        i = i + 1
    except StopIteration as si:
        print(f'Значение равно: {si.value}')
        break
