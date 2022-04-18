class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print(f"{self.name} says huff and puff, boy am I a fat slob")
        
    def rant(self):
        print(f"{self.name} says Epstien didn't kill himself")
        
class UI():
    def __init__(self, person):
        self.person = person
        
    def run_the_program(self):
        while True:
            response = input("What do you want to do? Run, Rant or Quit? ")
            if response.lower() == 'quit':
                break
            elif response.lower() == 'run':
                self.person.run()
            elif response.lower() == 'rant':
                self.person.rant()

## DRIVER CODE ##

#create Person

patrick = Person('Patrick', 24)
ui = UI(patrick)
ui.run_the_program()