
def bubble_sort(list):
    for i in xrange(len(list)):
        swapped = False
        for j in xrange(len(list)):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                swapped = True

        if not swapped:
            break

    return list

print bubble_sort([''])