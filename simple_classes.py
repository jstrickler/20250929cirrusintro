colors = []   # colors = list()
cities = list()
count = 27   #  count = int(27)
cities.append("Durham")
cities.append("Matamoros")
cities.append("Brownsville")
#  INSTANCE = CLASS()

class Breather:
    def breathe(self):  # not breed!
        print("breathing...")

class Animal:
    pass


class Dog(Breather, Animal):  # inherits from object
    def __init__(self, dog_name):  # constructor
        self.name = dog_name
        self.fur = "long"
        self._sex = None

    # getter property
    @property
    def sex(self):
        return self._sex

    # setter property
    @sex.setter    # d.sex = "male"
    def sex(self, value):
        if value not in ('male', 'female'):
            raise ValueError("Sex must be M or F")
        self._sex = value

    def bark(self):
        print(f"{self.name} says woof woof")

    def run(self):
        print("running running running")

if __name__ == "__main__":
    
    d = Dog("Nellie")
    d.bark()

    d2 = Dog("Andy")
    d2.bark()

    print(f"{d.name = }")
    print(f"{d2.name = }")
    print(f"{d.sex = }")  # d.sex()
    d.sex = "female"  # uses d.sex setter
    print(f"{d.sex = }")
    d.breathe()
    d2.breathe()
