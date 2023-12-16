```
    Класс Counter — это контейнер, предназначенный для подсчета числа сохраненных эквивалентных значений. 
    Он обеспечивает реализацию алгоритмов, для которых в других языках программирования обычно используют 
    мультимножества.
```

### Инициализация
```
    print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
    print(Counter({'a': 2, 'b': 3, 'c': 1}))
    print(Counter(a=2, b=3, c=1))
    
    >>> Counter({'b': 3, 'a': 2, 'c': 1})
    >>> Counter({'b': 3, 'a': 2, 'c': 1})
    >>> Counter({'b': 3, 'a': 2, 'c': 1})
```

### Изменение данных
```
    c = Counter()
    print('Initial :', c)  # Initial : Counter()

    c.update('abcdaab')
    print('Sequence:', c)  # Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

    c.update({'a': 1, 'd': 5})
    print('Dict :', c)  # Dict : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
```
