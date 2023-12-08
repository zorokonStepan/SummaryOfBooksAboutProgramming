def outer(func):
    print(f"Декорируется {func}")

    def inner(*args, **kwargs):
        print(f"Вызывается {func}(*{args}, **{kwargs})")
        value = func(*args, **kwargs)
        print(f"Возвращается {value}")
        return value

    return inner


def main(var: int = 0):
    if var:
        @outer
        def add_five(num):
            return num + 5
    else:
        def add_five(num):
            return num + 5
        add_five = outer(add_five)

    print(add_five)
    add_five(1)
    add_five(2)


if __name__ == "__main__":
    main(0)

    print('======================')

    main(1)
