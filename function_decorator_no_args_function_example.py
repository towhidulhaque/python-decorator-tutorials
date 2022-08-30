def my_decorator(f):
    print('my_decorator() called | function:' + str(f.__name__))

    def wrapped(*args, **kwargs):
        print('wrapped() called |  function:' + str(f.__name__) + ' | args:' + str(args) + '| kwargs:' + str(kwargs))
        f(*args)  # calling the original function

    return wrapped


@my_decorator
def display_function(a, b, c):
    print("display_function() called")


@my_decorator
def display_function_no_call(a, b, c):
    print("display_function_no_call() called")


print("Decoration finished for display_function() and display_function_no_call()")

display_function(1, 2, 3)
print("display_function() executed")

"""
output:

my_decorator() called | function:display_function
my_decorator() called | function:display_function_no_call
Decoration finished for display_function() and display_function_no_call()
wrapped() called |  function:display_function | args:(1, 2, 3)| kwargs:{}
display_function() called
display_function() executed
"""
