

# def sum(num1, num2=0): # parameters
#     res = num1 + num2
#
#     return res
#
# n1 = 5
# n2 = 9
#
# res1 = sum(n1) # arguments
# res2 = sum(res1, 1) * 2 # arguments
#
# print(res1)
# print(res2)


## indices (индекс)
##        0   1   2
# data = [10, 20, 30]
#
# data[1] = 133
#
# print(data[1])


# names = []
#
# while True:
#     name = input("Enter a name: ")
#
#     if name == "0":
#         break
#
#     names.append(name)
#
# print(names)

from random import randint

i = 0
values = []

while i < 10:
    rand = randint(10, 99)

    values.append(rand)

    i += 1

print(values)

### print all values 1 by 1
i = 0

while i < len(values):
    print(values[i])

    i += 1





