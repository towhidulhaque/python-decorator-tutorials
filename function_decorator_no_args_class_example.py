class MyClassDecorator(object):

    def __init__(self, f):
        print('__init__() called | function:' + str(f.__name__))
        self.f = f

    def __call__(self, *args, **kwargs):
        print('__call__() called | function:' + str(self.f.__name__) + ' | args: ' + str(args) + ' | kwargs:' + str(
            kwargs))
        self.f(*args, **kwargs)


@MyClassDecorator
def display_function(a, b, c):
    print("display_function() called")


@MyClassDecorator
def display_function_no_call(a, b, c):
    print("display_function_no_call() called")


print("Decoration finished for display_function() and display_function_no_call()")

display_function(1, 2, 3)
print("display_function() executed")

"""
output:

__init__() called | function:display_function
__init__() called | function:display_function_no_call
Decoration finished for display_function() and display_function_no_call()
__call__() called | function:display_function | args: (1, 2, 3) | kwargs:{}
display_function() called
display_function() executed
"""
