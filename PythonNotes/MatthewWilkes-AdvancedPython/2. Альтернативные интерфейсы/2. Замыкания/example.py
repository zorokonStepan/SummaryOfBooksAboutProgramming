def private_variable():
    value = None

    def set(new_value):
        nonlocal value
        value = new_value

    def get():
        return value

    return set, get


if __name__ == "__main__":
    a_set, a_get = private_variable()
    b_set, b_get = private_variable()

    print(a_get, a_set, sep='\n')
    print(b_get, b_set, sep='\n')

    a_set(10)
    print(f"a={a_get()} b={b_get()}")

    b_set(4)
    print(f"a={a_get()} b={b_get()}")

