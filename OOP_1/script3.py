class Animal: # base class, parent class, super class
    def __init__(self, name, color): # magic method (constructor)
        self.__name = name
        self.color = color

    def getName(self):
        return self.__name

    def setName(self, newName):
        if not newName[0].isupper() or not newName.isalpha():
            raise ValueError("Incorrect Name")

        self.__name = newName

    def voice(self):
        print("Unknown voice :<")

class Cat(Animal): # derived class, child class
    def __init__(self, name, color):
        super().__init__(name, color)

        self.__speed = 100

    def voice(self):
        print("Meow-meow!")

    def getSpeed(self):
        return self.__speed

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def voice(self):
        # super().voice()
        print("Bark-bark!")

cat1 = Cat("Tika", "white")

cat1.voice()
print(cat1.getName())

dog1 = Dog("Doggy", "red")

dog1.voice()
print(dog1.getName())


# animal1 = Animal("Tarlan", "Black")
# animal2 = Animal("Atin", "Purple")
#
# animal1.setName("Murad")
#
# print(animal1.getName())



# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     def display(self):
#         print(f"{self.name}: {self.__price}")
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, value):
#         if value <= 0:
#             raise ValueError("Price must be greater than 0")
#
#         self.__price = value
#
# prod1 = Product("Pomidor", 2)
# prod2 = Product("Cucumber", 2.2)
#
# prod1.set_price(prod1.get_price() * -0.9)

# __price = __price * 0.9

# prod1.display()
# prod2.display()


