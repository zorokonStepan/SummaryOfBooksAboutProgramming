## Определение
```
        Ввиду того что экземпляры namedtuple не используют словарей, их эффективность в отношении использования памяти 
    та же, что и у экземпляров обычных кортежей. Каждый тип именованного кортежа представляется собственным классом, 
    который создается c помощью функции-фабрики namedtuple().

    Аргументами этой функции являются имя нового класса и строка, содержащая имена элементов.
        
        Person = namedtuple('Person', 'name age')
        bob = Person(name='Bob', age=30)
        print('\nRepresentation:', bob)  # Representation: Person(name='Bob', age=30)
        
        jane = Person(name='Jane', age=29)
        print('\nField by name:', jane.name)  # Field by name: Jane
```