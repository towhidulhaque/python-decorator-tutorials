def register(*decorators):
    """
    This decorator is for chaining multiple decorators.
    :param decorators:args(the decorators as arguments)
    :return: callable object
    """

    def register_wrapper(func):
        for deco in decorators[::-1]:
            func = deco(func)
        func._decorators = decorators
        return func

    return register_wrapper


def deco1(f):
    def wrapper(*args, **kwds):
        print('-' * 100)
        fn = f(*args, **kwds)
        print('-' * 100)
        return fn

    return wrapper


def deco2(f):
    def wrapper(*args, **kwds):
        print('*' * 100)
        fn = f(*args, **kwds)
        print('*' * 100)
        return fn

    return wrapper


def deco3(f):
    def wrapper(*args, **kwds):
        print('#' * 100)
        fn = f(*args, **kwds)
        print('#' * 100)
        return fn

    return wrapper


class Foo(object):
    @deco1
    @deco2
    @deco3
    def bar(self):
        print('I am bar')


class AnotherFoo(object):
    @register(deco1, deco2, deco3)
    def bar(self):
        print('I am bar')


foo = Foo()
foo.bar()
print('\n\n~~~~ Alternate Way to Annotate ~~~~\n\n')
another_foo = AnotherFoo()
another_foo.bar()
print(another_foo.bar._decorators)


"""
output:

----------------------------------------------------------------------------------------------------
****************************************************************************************************
####################################################################################################
I am bar
####################################################################################################
****************************************************************************************************
----------------------------------------------------------------------------------------------------


~~~~ Alternate Way to Annotate ~~~~


----------------------------------------------------------------------------------------------------
****************************************************************************************************
####################################################################################################
I am bar
####################################################################################################
****************************************************************************************************
----------------------------------------------------------------------------------------------------
(<function deco1 at 0x7f50c7e6c940>, <function deco2 at 0x7f50c7e6c9d0>, <function deco3 at 0x7f50c7e6ca60>)

"""