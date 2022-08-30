def my_decorator(*deco_args, **deco_kwargs):
    print('my_decorator() called | args: ' + str(deco_args) + ' | kwargs:' + str(deco_kwargs))

    def inner(f):
        print('inner(f) called  |  function:' + str(f.__name__) + ' || ( Have access to  deco_args: ' + str(
            deco_args) + ' | deco_kwargs:' + str(deco_kwargs) + ')')

        def wrapped(*args, **kwargs):
            print(
                'wrapped() called |  function:' + str(f.__name__) + ' | args:' + str(args) + '| kwargs:' + str(
                    kwargs) + ' || ( Have access to  deco_args: ' + str(
                    deco_args) + ' | deco_kwargs:' + str(deco_kwargs) + ')')
            return f(*args, **kwargs)  # calling the original function and return

        return wrapped

    return inner


@my_decorator("arg1", "arg2")
def display_function(a, b, c):
    print("display_function() called")


@my_decorator("no_call_arg1", "no_call_arg2")
def display_function_no_call(a, b, c):
    print("display_function_no_call() called")


print("Decoration finished for display_function() and display_function_no_call()")

display_function(1, 2, 3)
print("display_function() executed")

"""
output:

my_decorator() called | args: ('arg1', 'arg2') | kwargs:{}
inner(f) called  |  function:display_function || ( Have access to  deco_args: ('arg1', 'arg2') | deco_kwargs:{})
my_decorator() called | args: ('no_call_arg1', 'no_call_arg2') | kwargs:{}
inner(f) called  |  function:display_function_no_call || ( Have access to  deco_args: ('no_call_arg1', 'no_call_arg2') | deco_kwargs:{})
Decoration finished for display_function() and display_function_no_call()
wrapped() called |  function:display_function | args:(1, 2, 3)| kwargs:{} || ( Have access to  deco_args: ('arg1', 'arg2') | deco_kwargs:{})
display_function() called
display_function() executed
"""
