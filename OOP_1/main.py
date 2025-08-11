class Animal:
    def __init__(self, name, color): # magic method (constructor)
        self.__name = name
        self.color = color

    def voice(self):
        print(f"{self.__name}: Roar!!!")

    def getName(self):
        return self.__name

    def setName(self, newName):
        if not newName[0].isupper() or not newName.isalpha():
            raise ValueError("Incorrect Name")

        self.__name = newName


animal1 = Animal("Tarlan", "Black")
animal2 = Animal("Atin", "Purple")

animal1.setName("Murad")

print(animal1.getName())


