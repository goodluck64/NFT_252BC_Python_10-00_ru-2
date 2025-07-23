# def change(x):
#     x = 42
#
# value = 10
#
# change(value)
#
# print(value)
#############
# def addToList(collection: list):
#     collection.append("Alex")
#     collection.append("Ela")
#
#     collection = ["Hello"]
#
#     collection.pop()
#
#
# names = ["Test"]
#
# addToList(names)
#
# print(names)
#########
# def getUserData():
#     age = 18
#     name = "Ela"
#
#     return age, name
#
#
# data = getUserData()
#
# print(data)
# print(data[0])
# print(data[1])
#
# print("-" * 16)
#
# age, name = getUserData()
#
# print(age)
# print(name)
###################
from random import randint

# def printValues(*args):
#     for item in args:
#         print(item)
#
#
# values = (10, 20, "test")
#
# printValues(*values)


# x = [10, 20, 30, 40]
#
# print(*x, sep='|')


##############

x = 10

def change():
    global x
    x = 42


change()
print(x)



def generate_rn():
    while True:
        number = randint(1000, 9999)
        strNumber = str(number)
        flag = False

        for char in strNumber:
            if strNumber.count(char) > 1:
                flag = True
                break

        if not flag:
            return number



for i in range(50):
    print(generate_rn())