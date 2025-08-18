def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def show_calculation(func):
    a = int(input())
    b = int(input())

    if func is not None:
        print(func(a, b))



currentFunc = None

choice = int(input())

if choice == 1:
    currentFunc = add
elif choice == 2:
    currentFunc = subtract
elif choice == 3:
    currentFunc = lambda a, b: a * b

show_calculation(currentFunc)

