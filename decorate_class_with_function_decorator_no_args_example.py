def my_decorator(_class):
    print('my_decorator() called for the class: ' + str(_class.__name__))

    # define a new display method
    def new_display(self):
        print('new_display() called')
        print('Name: ', self.name)
        print('PIN: 1234')

    # replace the display with new_display
    # (if the display method did not exist in the class,
    # the new_display would have been added to the class as the display method)
    _class.display = new_display

    # return the modified employee
    print('returning modified class (not object)')
    return _class


@my_decorator
class Employee:
    def __init__(self, name):
        print('original __init__() called' + ' | arg:' + str(name))
        self.name = name

    def display(self):
        print('original display() called')
        print('Name:', self.name)


print("Decoration finished for Employee Class")
obj = Employee('Towhidul Haque Roni')
print("Employee obj created")
obj.display()
print("display() executed")

"""
output:

my_decorator() called for the class: Employee
returning modified class (not object)
Decoration finished for Employee Class
original __init__() called | arg:Towhidul Haque Roni
Employee obj created
new_display() called
Name:  Towhidul Haque Roni
PIN: 1234
display() executed
"""