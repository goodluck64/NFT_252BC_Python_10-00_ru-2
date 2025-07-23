# str, int, bool, float, range, tuple
# list, dict

#############################
### Create tuple
#          0       1   2
# mytuple = ("Alex", 42, True)

# i = mytuple.index(42)

# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])

### Unpacking
# a, b, c = mytuple
#
# print(a, b, c)

### Convert tuple to list
# list1 = list(mytuple)
#
# print(list1)

### Modify list
# list1[1] = 99


### Convert back to tuple
# mytuple = tuple(list1)
#
# print('-' * 10)


# def get_data():
#     return "Alex", 42, True


#############################

### Dictionaries
# translates = {
#     "en-ru": {
#         "apple": "яблоко",
#         "car": "машина",
#         "brother": "брат",
#         "plant": ("растение", "завод")
#     },
#     "ru-az": {
#         "яблоко": "alma",
#         "машина": "mashin",
#         "брат": "gardash",
#         "растение": "bitki",
#         "завод": "zavod"
#     }
# }

# print(translates["en-ru"]["plant"][1])




def print_person(person):
    print("First Name:", person["name"])
    print("Age:", person["age"])
    print("Height:", person["height"])


def change_person_age(person):
    person["age"] += 1


data = {
    "name": "Alex",
    "age": 89,
    "height": 178
}

# change_person_age(data)
# print_person(data)

# a, b = ('name', 'Alex')


### Iterate dictionary
# for k, v in data.items():
#     print(f"{k}: {v}")

# for key in data:
#     print(f"{key}: {data[key]}")

### Methods

## Add pair
# data["iq"] = 95
#
# print(data)

## Remove pair
# if "iq" in data:
#     del data["iq"]

# print(data)

## Remove pair 2
# if "age" in data:
#     data.pop("age")
#
# print(data)

## get method
# print(data["name"]) ## error
# print(data.get("name")) ## no error

## keys & values
# keys = data.keys()
#
# print(keys)
#
# values = data.values()
#
# print(values)

## popitem (delete last added key)

# print(data)
# data.popitem()
# print(data)


# [('name', 'Alex'), ('age', 89), ('height', 178)]




