def square_decorator(func):
    def wrapper(a, b):
        result = func(a, b)
        return result ** 2

    return wrapper


@square_decorator
def add(a, b):
    return a + b


print(add(3, 4))