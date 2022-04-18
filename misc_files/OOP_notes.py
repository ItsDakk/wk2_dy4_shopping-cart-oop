# Object Orientated Programming in Python

def hello():
    print("hello")

x = 1
print(type("hello")) # This is telling us that's hello is an object of the class 'str'
print(type(x)) # This is object of the class <int>

print(type(hello)) # Object of class function

x = 1
y = "hello"

# print(x + y) # This will produce an error because it doensn't know how to add class of 'int' with class of 'str'

string = "hello"
print(string.upper()) # We can use this method that is acting on a specific object. .upper() works with class obj <str>

## Create our own class ##

class Dog:              # This is a blueprint for the class of Dog
    # A method is just a function that goes in a class as so - we are creating our own methods to be called
    
    def add_one(self, x): # We can have these methods take in parameters 
        return x + 1    # Can return we don't have to print.
    
    def bark(self): # This is a method 
        print("bark")

#d = Dog() # Variable d is assigned to instance class <Dog>
#d.bark()
#print(type(d)) # The module we run is <__main__.Dog>

 #print(d.add_one(5))


## self method## 

class Dog:   # Blueprint for how a 'Dog' actually works            
    
    def __init__(self, name, age):   # Has 2 underscores - the 'init' allows instantiate the object when it's created
        self.name = name        # We have created an attribue of the class dog which is name (attribute called name)
        self.age = age          # Equal to whatever age we pass in

    def get_name(self):         # The first parameter will always be 'self' because we have to pass on object itself
        return self.name

    def get_age(self):         
        return self.age

    def set_age(self, age):     # Allows us to modify certain attributes      
        self.age = age

d = Dog("Tim", 34)                     # This will pass the method to 'init' instanly - these are stored permantely
d.set_age(23)                           # Can change values of the stored methods as so (set_age)
print(d.get_age())



#d2 = Dog("Bill", 14)                    # 2 different dog names that stores each object
#print(d2.get_age())

# Objects are for multiple uses #





