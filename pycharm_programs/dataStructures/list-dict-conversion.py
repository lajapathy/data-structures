
list1 = [{1:2, 3:4}, {5:6}]


def list_to_dict(list1):
    new_keys = [item for sublist in list1 for item in sublist]
    print new_keys


list_to_dict(list1)
