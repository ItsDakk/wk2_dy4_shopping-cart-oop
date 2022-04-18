#Exercise 2 - 
# Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case

# class Exercise():

#     def get_string():
#          pass

#     def print_string():
#         pass


# class Exercise():
#     def __init__(self):
#         pass
    
#     def get_string(self):
#         input("Enter text here")
        
#     def print_string(self):
#         print(f"This is what you entered: ")
        
# test = Exercise()

# test.get_string()
# test.print_string()
        
class Exercise():
    def __init__(self):
        pass
    
    def get_string(self):
        return input("Enter text here")
        
    def print_string(self, output):
        print(f"This is what you entered: {output}.") # Need to return as upper case
        
test = Exercise()

name = test.get_string()
test.print_string(name)  