def isBST(root, arr=[]):
    # Code here

    if root.left:
        arr.append(isBST(root.left, arr))
    arr.append(isBST(root.data))
    if root.right:
        arr.append(isBST(root.right, arr))

    def is_increasing(array):
        increasing = True
        i = 0
        while (i < len(array) - 1):
            if array[i + 1] < array[i]:
                increasing = False

    return is_increasing(arr)

isBST()