num_list = [0, 1, 0, 4, 3]


def move_zeroes(list1):
    count = 0
    new_list = []
    for i in list1:
        import pdb;pdb.set_trace()
        if i == 0:
            count = count + 1
        else:
            new_list.append[i]

    for num in range(0, count):
        new_list.append(0)

    return new_list


new_list = []
new_list = move_zeroes(num_list)

print(new_list)