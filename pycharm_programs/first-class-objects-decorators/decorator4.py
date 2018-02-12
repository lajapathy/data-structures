from decorator3 import my_decorator

@my_decorator
def just_come_function():
    print('ssss')

just_come_function()
##### @my_decorator is just an easier way of saying just_some_function = my_decorator(just_some_function)