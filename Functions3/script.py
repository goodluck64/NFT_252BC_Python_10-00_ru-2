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