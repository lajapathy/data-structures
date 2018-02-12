### nonlocal works only in Python 3 !!!

def outside():
    msg = "Outside!"

    def inside():
        nonlocal msg
        msg = "Inside!"
        print(msg)

    inside()
    print(msg)


def outside():
    msg = "Outside!"

    def inside():
        nonlocal msg
        msg = "Inside!"
        print(msg)

    inside()
    print(msg)

