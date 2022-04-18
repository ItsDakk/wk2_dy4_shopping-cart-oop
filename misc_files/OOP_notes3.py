class Pet: # GENERAL CLASS # This is going to contain the functionality that we want the dog and cat class to have
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def show(self):
            print(f"I am {self.name} and I am {self.age} years old")

        def speak(self):
            print("I don't know what I say")


class Cat(Pet):              # SPECIFIC # This is inheriting the the generalized Pet class
    def __init__(self, name, age, color):
        super().__init__(name,age) # 'Super' stands for inheriting the super-class (Pet) We have to call this line again incase the super class has something special
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):              # SPECIFIC # This is inheriting the the generalized Pet class
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Red")
c.show()                # Even though there was no 'init' method in the Cat class, it inherited that attribute from the Pet class
c.speak() 
d = Dog("Jill", 12)
d.show()
d.speak()               # Even though there is a 'speak' method in class Pet - the 'child' class of Dog is more specific therefore overriding the Pet speak attribute


