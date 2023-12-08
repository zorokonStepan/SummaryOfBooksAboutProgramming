def add_integer_to_all_arguments(offset):
    def decorator(func):
        def inner(*args):
            args = [arg + offset for arg in args]
            return func(*args)
        return inner
    return decorator


@add_integer_to_all_arguments(10)
def power(x, y):
    return x ** y


# @add_integer_to_all_arguments(3)
# def add(x, y):
#     return x + y

def add(x, y):
    return x + y


add = add_integer_to_all_arguments(3)(add)


if __name__ == "__main__":
    print(power)
    print(power(0, 0))

    print("===================================")

    print(add)
    print(add(0, 0))
