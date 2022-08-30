class MyClassDecorator:
    # accept the class as argument
    def __init__(self, _class):
        print('__init__() called | class:' + str(_class.__name__))
        self._class = _class

    # accept the class's __init__ method arguments
    def __call__(self, name):
        print('__call__() called | class:' + str(self._class.__name__) + ' | arg:' + str(name))

        # define a new display method
        def new_display(self):
            print('new_display() called')
            print('Name: ', self.name)
            print('PIN: 1234')

        # replace display with new_display
        self._class.display = new_display

        # return the instance of the class
        obj = self._class(name)
        print('returning modified class object')
        return obj


@MyClassDecorator
class Employee:
    def __init__(self, name):
        print('original __init__() called' + ' | arg:' + str(name))
        self.name = name

    def display(self):
        print('original display() called')
        print('Name: ', self.name)


print("Decoration finished for Employee Class")
obj = Employee('Towhidul Haque Roni')
print("Employee obj created")
obj.display()
print("display() executed")

"""
output:

__init__() called | class:Employee
Decoration finished for Employee Class
__call__() called | class:Employee | arg:Towhidul Haque Roni
original __init__() called | arg:Towhidul Haque Roni
returning modified class object
Employee obj created
new_display() called
Name:  Towhidul Haque Roni
PIN: 1234
display() executed
"""
