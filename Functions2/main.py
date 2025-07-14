#### Functions
##         0   1   2   3   4   5
# mylist = [10, 40, 42, 51, 68, 13]
# mylist2 = [11, 12, 13, 14, 15, 16]
#
# def search(items, value): # parameters
#     for i in range(len(items)):
#         if items[i] == value:
#             return i
#     return -1
#
#
# idx = search(mylist, 42) # arguments
#
# mylist[idx] *= 0.95
#
# print(mylist[idx])

# print(mylist[idx])

# search(mylist2, 15) # arguments

#### Global vs Local

# x = 42 # global variable
#
# def change():
#     global x
#
#     x = 9 # global variable
#
#     print(x)
#
# change()
#
# print(x)

#### *args
# def add(*args): # tuple
#     sum = 0
#     for item in args:
#         sum += item
#
#     return sum
#
#
# result = add(10, 11, 12, 13, 14, 15, 13)
#
# print(1, 2, 3, 4, 5, 6, 7, 8)

#### named arguments

# def print_values(a, b, c):
#     print(f"a = {a}")
#     print(f"b = {b}")
#     print(f"c = {c}")
#
# print_values(b=10, c=30, a=20)


a = [10, 20, 30, 11, 12]

print(min(a))