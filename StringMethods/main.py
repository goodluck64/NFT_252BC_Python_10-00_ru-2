# items = ["Pomidor", "Xiyar", "Kartof"]
# prices = [44, 10, 20]

# for i in range(len(items)):
#     items[i] = "Test"

# print(items)

# items.pop()
# prices.pop()

# items.insert(1, "Onion")
# items.index("Kartof")

# print(items)

#

# 00001111 = 15
# 00011110 = 15 + 31 = 46
# 01010100
#

# byte, sbyte, short, ushort, int, uint, long, ulong

# concatenation - конкатенация (сложение двух строк в одну)
# s = "Hello " + "world!"
#
# print(s)

### rindex, index, count
# s = "Some text"
#
# result1 = s.index("t")
# result2 = s.rindex("t")
# result3 = s.count("t")
#
# print(result1)
# print(result2)
# print(result3)

### indexer (индексатор [])
# s = "Some text"
#
# # s[0] = "s" # error
#
# print(s[0])

### replace
# s = "Goodbye world!"
#
# newStr = s.replace("Goodbye", "Hello")
#
# print(s)
# print(newStr)


### isalpha,
# text = "123"

# if text.isalpha():
#     print("All symbols are alphabet")
# else:
#     print("not alphabet")

# if text.isalnum():
#     print("All symbols are alphabet or numbers")
# else:
#     print("nor alphabet and numbers")

### isdigit, isdecimal, isnumeric
# if text.isdigit():
#     print("all digit")
# else:
#     print("not all digit")


### islower and isupper
# text = "hello world"
#
# if text.islower():
#     print("lower")
# else:
#     print("not lower")

### upper, lower, capitalize

# text = input()

# upperText = text.upper()
# lowerText = text.upper()
# capitalizedText = text.capitalize()

# print(upperText)
# print(lowerText)

# print(capitalizedText)


### strip

# text = "\t   Hello how are you?  "
#
# stripped = text.lstrip()
#
# print(stripped)

### startswith & endswith

# text = "Hello"
#
# if text.endswith("o"):
#     print("OK")
#
# if text.startswith("He"):
#     print("OK")


### split & join

# text = input() # Hello how are you my friend?
#
# result = text.split(" ")
#
# words = len(result)
#
# print(words)
# print(result)
#
# joined = "-".join(result)
#
# print(joined)


### in operator

# text = "hello"
#
# if "o" in text:
#     print("o is in text")


### remove text

# text = "Hello world!"
#
# newStr = text.replace(" ", "")
#
# print(newStr)

# s = 82
#
# print(chr(s))
# print(ord('B'))



# oldStr = "hello"

# s[0] = "H"

# newStr = oldStr.capitalize()
#
# print(oldStr)
# print(newStr)


print("Hello" * 2)
