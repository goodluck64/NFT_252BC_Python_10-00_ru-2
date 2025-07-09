## immutable sample
# a = 10
# b = a
#
# b = 9
#
# print(a)
#############
## mutable sample
# a = [42, 13]
# b = a
#
# b.append(9)
#
# print(hex(id(a)))
# print(hex(id(b)))
#
# print(a) #
# print(b) #

## immutable data types
## int, float, bool str

## mutable data types
## list


## range sample

# r = range(10) # 0 1 2 3 ... 9
# r = range(5, 10) # 5 6 7 8 9
# r = range(-10, 10) # -10 ... 10
# r = range(0, 20, 5) #
#
# mylist = list(r)
#
# print(mylist)

############# for loop
# numbers = [11, 33, 40, 50]

# i = 0
#
# while i < len(numbers):
#     numbers[i] *= 2
#
#     i += 1

# for item in numbers:
#     item *= 2
#
# print(numbers)


############# for loop 2

# numbers = [9, 10, 11, 12]
#
# for i in range(len(numbers)):
#     print("Number =", numbers[i], i)
#     # print(f"Number = {numbers[i]}; index = {i}")
#


### append

# l = [1, 2, 3]
#
# l.append(9)
#
# print(l)

### insert

# mylist = [10, 20, 30, 40]
#
# mylist.insert(1, 9)
#
# print(mylist)

### pop

# mylist = [10, 9, 13, 42, 69]
#
# mylist.pop()
# mylist.pop(1) # 10, 13, 42, 69
# mylist.pop(2) # 10, 13, 69
#
# print(mylist)

### remove

# names = ["Alex", "Rafa", "Ela", "Mika", "Alex"]
# name_to_remove = input()
#
# if name_to_remove in names: # <---- check
#     names.remove(name_to_remove) # <------ remove
# else:
#     print("name not found")
#
# print(names)


### clear
# mylist = [10, 9, 13, 42, 69]
#
# mylist.clear()
#
# print(mylist)

### sort

# mylist = [10, 9, 13, 42, 69]
#
# mylist.sort(reverse=True)
#
# print(mylist)

### count
# mylist = [10, 9, 13, 9, 42, 69, 9, 9]
#
# result = mylist.count(9)
#
# print(result)

### extend

# mylist = [10, 13, 42, 9]
#
# mylist.extend([1, 2, 3])
#
# print(mylist)

### +

# mylist1 = [1, 2, 3]
# mylist2 = [4, 5, 6]
# mylist3 = mylist1 + mylist2
#
# print(mylist1)
# print(mylist2)
# print(mylist3)

### index

# mylist = [10, 13, 9, 42, 69, 9, 9]
#
# idx = mylist.index(30)
#
# mylist[idx] += 1
#
# print(mylist)

