## Arithmetic operators
# +, -, /, *, //, %

## Assignment operators (shorthand operators)
# =, +=, -=, /=, *=, //=, %=

# a = 5
#
# # a = a % 2
# a %= 2
#
# print(a)


## Comparison operators
# >  - greater (больше)
# >= - greater or equals (больше или равно)
# <  - less (меньше)
# <= - less or equals (меньше или равно)
# == - equals (равно)
# != - not equals (не равно)

# a = int(input())

# result = a % 2
# print(result)

## is even or odd

# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
# a = 0

# if a > 0:
#     print("positive")
# elif a < 0:
#     print("negative")
# else:
#     print("zero")
########################
# a = int(input())
#
# if a % 2 == 0:
#     if a > 0:
#         print("even positive")

## Logical operators
# and (logical multiplication)
# or (logical addition)
# not (inversion)

## and table
## 1 * 0 => 0 (False)
## 0 * 1 => 0 (False)
## 0 * 0 => 0 (False)
## 1 * 1 => 1 (True)

## or table
## 1 + 0 => 1 (True)
## 0 + 1 => 1 (True)
## 0 + 0 => 0 (False)
## 1 + 1 => 1 (True)

## not table
# not True => False
# not False => True

# a = False
# b = True
#
# result = a and b # 1 + 1 => 1 (False)
#
# print(result)

#########
# a = 4
#
# if a > 5:
#     print("a > 5")






op = input()

if op == "+":
    print("addition")
elif op == "-":
    print("subtraction")
else:
    print("invalid input")









