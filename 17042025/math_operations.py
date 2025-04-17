def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Cannot divide by zero")


print(__name__)
if __name__ == "__main__":
    for i in range(5):
        print(i)
