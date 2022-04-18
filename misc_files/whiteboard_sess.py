# David and Andrew need to meet me after class
# Felix and Jessica need to do more Codewars
# Robert and William and John need to finish their homework
# and everybody else is good to go.

# Write a function that takes a students name as an argument and returns what that student needs to do.  
# Make sure to make the name argument case-insensitive
# If the person in not in the class return "Get Out of My Class"

#ex) what_to_do("David") returns: "Meet With Me After Class"
#ex) what_to_do("Joe") returns: "Get Out Of My Class"
#ex) what_to_do("Saed") returns: "You are Good to Go!"
#ex) what_to_do("felix") returns: "Do More Code Wars"
#ex) what_to_do("john") returns: "Finish your Homework"


students=["Andrew","Apollo","Cole","David","Dereck","Felix","Jessica","John", "Robert", "Saed", "Tony", "William" ]

def classmates(name):
    for student in students:
        if student == "David".lower():
            return "Meet With Me After Class"
        elif student == "Joe":
            return "Get Out Of My Class"
        elif student == 'Saed':
            return "You are Good to Go"
        elif student == 'felix':
            return "Do More Code Wars"
        elif student == 'john':
            return "Finish your Homework"
        return "Get Out of My Class"
    return students
        
print(classmates('felix'))

def classmates(name):
    new_dictionary = {

    'Andrew': 'meet me after class',
    'David': 'meet me after class',
    'Felix': 'need to do more Codewars',
    'Jessica': 'need to do more Codewars',
    'Robert': 'finish their homework',
    'William': 'finish their homework',
    'John': 'finish their homework',
    'Apollo': 'good to go',
    'Cole': 'good to go',
    'Dereck': 'good to go',
    'Saed': 'good to go',
    'Tony': 'good to go',

}
    return new_dictionary.get(name.title(), 'get out of my class')
print(classmates('apollo'))
