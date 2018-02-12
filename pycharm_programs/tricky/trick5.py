class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

# Static variables are stored as dictionaries.
# When a child overwrites the value of a variable, a new entry is made to this dictionary
# When a child hasnt overwritten the value of a variable yet, the value obtained for the variable is
# whatever the parent class currently has
