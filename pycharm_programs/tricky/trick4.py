def multipliers():
    return [lambda x: i * x for i in range(4)]


print multipliers()
print [m(2) for m in multipliers()]