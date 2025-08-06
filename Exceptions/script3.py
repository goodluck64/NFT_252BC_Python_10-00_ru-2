# nums = [10, 20, 30]
#
# elem = 42
#
# try:
#     nums.remove(elem)
#
#     print("Deleted")
# except:
#     print("Element not found")

## ValueError
## ZeroDivisionError

# try:
#     a = int(input())
#     b = int(input())
#
#     print(a / b)
# except ValueError:
#     print("You have entered wrong value(s).")
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except:
#     print("Something went wrong.")

# print("Exit...")

value = None

while True:
    try:
        value = int(input("Enter a number: "))

        break
    except ValueError:
        print("Enter a number, you, dumb!")



print(f"Value = {value}")


names = []

def add_name(name):
    if not name[0].isupper():
        raise ValueError("Name must start with a capital letter")

    names.append(name)

# throw

try:
    add_name("Alex")
    add_name("ela")
except ValueError as err:
    print(err)

print(names)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero")

    return a / b

try:
    a = int(input())
    b = int(input())

    result = divide(a, b)

    print(result)
except ZeroDivisionError as err:
    print(err)