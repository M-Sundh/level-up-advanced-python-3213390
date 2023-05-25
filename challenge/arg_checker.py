import functools


def arg_checker(*arg_types):
    '''An argument checker decorator that checks both:
        - The number of variables that you use for a function
        - The type of each variable.
       Raises a TypeError if either of these fail'''
    def decorator_arg_checker(func):
        def wrapper_arg_checker(*args,**kwargs):
            if tuple(map(type,args)) != arg_types:
                print("not all")
                raise TypeError
            return func(*args,**kwargs)
        wrapper_arg_checker.__name__ = func.__name__
        wrapper_arg_checker.__doc__ = func.__doc__
        return wrapper_arg_checker
    return decorator_arg_checker


@arg_checker(int, int, int, int)
def summa(a, b, c, d):
    "Summa string"
    return a+b+c+d

print(summa(1, 2, 3, 4))
print(summa.__name__)
print(summa.__doc__)
