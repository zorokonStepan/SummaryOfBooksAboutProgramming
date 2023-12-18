import itertools
import collections
import multiprocessing


class SimpleMapReduce:
    def __init__(self, map_func, reduce_func, num_workers=None):
        """
            map_func
                Функция для отображения входных данных на промежуточные.
                Получает один аргумент в качестве входного значения и возвращает кортеж c ключом и значением для свертки.

            reduce_func
                Функция для свертки сгруппированной версии промежуточных данных в финальный вывод.
                В качестве аргумента получает ключ, созданный map_func, и последовательность значений, связанных с этим
                ключом.

            num_workers
                Число создаваемых рабочих процессов в пуле.
                По умолчанию равно числу процессоров текущего хоста.
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        """
            Организует отображаемые значения по ключам.
            Возвращает неотсортированную последовательность кортежей c ключом и последовательностью значений.
        """
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        """
            Обработать входные значения через предоставленные функции отображения и свертки.

            inputs
                Итерируемый объект, содержащий входные данные для обработки.
            chunksize=1
                Фрагмент входных данных для передачи каждому рабочему процессу.
                Это можно использовать для настройки производительности во время фазы отображения.
        """
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values
