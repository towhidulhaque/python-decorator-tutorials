class MyClassDecorator(object):

    def __init__(self, *deco_args, **deco_kwargs):
        print('__init__() called  | args: ' + str(deco_args) + ' | kwargs:' + str(deco_kwargs))

    def __call__(self, f):
        print('__call__() called | function:' + str(f.__name__))

        def wrapped(*args, **kwargs):
            print(
                'wrapped() called |  function:' + str(f.__name__) + ' | args:' + str(args) + '| kwargs:' + str(kwargs))
            return f(*args, **kwargs)

        return wrapped


@MyClassDecorator("arg1", "arg2")
def display_function(a, b, c):
    print("display_function() called")


@MyClassDecorator("no_call_arg1", "no_call_arg2")
def display_function_no_call(a, b, c):
    print("display_function_no_call() called")


print("Decoration finished for display_function() and display_function_no_call()")

display_function(1, 2, 3)
print("display_function() executed")

"""
output:

__init__() called  | args: ('arg1', 'arg2') | kwargs:{}
__call__() called | function:display_function
__init__() called  | args: ('no_call_arg1', 'no_call_arg2') | kwargs:{}
__call__() called | function:display_function_no_call
Decoration finished for display_function() and display_function_no_call()
wrapped() called |  function:display_function | args:(1, 2, 3)| kwargs:{}
display_function() called
display_function() executed
"""
