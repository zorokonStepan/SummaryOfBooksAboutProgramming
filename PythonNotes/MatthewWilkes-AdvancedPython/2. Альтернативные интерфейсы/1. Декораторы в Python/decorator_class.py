class add_integer_to_all_arguments:
    def __init__(self, offset):
        self.offset = offset

    def __call__(self, func):
        def inner(*args):
            args = [arg + self.offset for arg in args]
            return func(*args)
        return inner


# def add_integer_to_all_arguments(offset):
#     def decorator(func):
#         def inner(*args):
#             args = [arg + offset for arg in args]
#             return func(*args)
#         return inner
#     return decorator
