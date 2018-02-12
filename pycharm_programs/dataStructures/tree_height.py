


def getHeight(root):
    if not root:
        return 0
    return max(1 + getHeight(root.left) ,1 + getHeight(root.right))