# dunder (double underscore)
# magic methods

## Constructor and destructor
# __init__, __del__

## string magic methods
# __repr__, __str__

## arithmetic magic methods
# __add__ (+)
# __sub__ (-)
# __mul__ (*)
# __truediv__ (/)
# __floordiv__ (//)
# __mod__ (%)
# __pow__ (**)

## comparison magic methods
# __eq__ equals (==)
# __ne__ not equals (!=)
# __lt__ less than (<)
# __le__ less equals (<=)
# __gt__ greater than (>)
# __ge__ greater equals (>=)

## collection magic methods
# __len__, __getitem__, __setitem__, __delitem__, __contains__


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        newX = self.x + other.x
        newY = self.y + other.y

        return Point(newX, newY)

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Object:
    def __init__(self):
        self.__file = open("data.txt", "w")

        print("Constructor")

    def __del__(self):
        print("Destructor")

        self.__file.close()

class Stock:
    def __init__(self):
        self.__items = ["Onion", "Pomidor", "GPU"]
        self.__reserved = ["PC", "Phone", "Remote"]

    def __contains__(self, value):
        return self.__items.count(value) > 0

    def __len__(self):
        return len(self.__items) + len(self.__reserved)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, value):
        self.__items[index] = value

    def __delitem__(self, index):
        try:
            self.__items.pop(index)
        except:
            pass

    def __repr__(self):
        return f"{type(self)}: ({self.__items})"

    def __str__(self):
        return f"Stock: {self.__reserved}"

p1 = Point(10, 20)
p2 = Point(30, 40)
p3 = Point(10, 20)

print(p1 + p2)

if p1 == p3:
    print("equals")
else:
    print("not equals")

#####################
# obj = Stock()
#
# print(str(obj))
# print(repr(obj))

#####################
# obj = Stock()
#
# if "Onion" in obj:
#     print("Onion is in stock")

# print(len(obj))

# obj[1] = "Cucumber"
#
# print(obj[1])
#
# del obj[1]
#
# print(obj[1])


#####################

# obj = Object()
#
# input("Before None")
#
# del obj
#
# input("After None")