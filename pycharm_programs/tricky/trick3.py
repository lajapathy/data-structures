
def function(data=[]):
    data.append(1)
    return data

print function()
print id(function())
print function()
print id(function())
print function()
print id(function())
