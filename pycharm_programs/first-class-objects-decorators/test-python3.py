
def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))

def call_foo_with_arg(fun_name,arg_value):
    return fun_name(arg_value)


print (call_foo_with_arg(foo,5))