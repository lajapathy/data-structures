class StatsTreeNode(object):
    # Class variable
    _id = 0

    # initializes a node
    def __init__(self, data, parent=None, level=0):
        self.data = data
        self.children = []
        self.parent = parent
        self.level = level
        self.id = StatsTreeNode._id
        StatsTreeNode._id += 1

    # Adds childObj as a child to the current Node
    def addChild(self, childObj):
        self.children.append(childObj)

    def getNodeData(self):
        return self.data

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def getLevel(self):
        return self.level

    # This method prints all children of the current Node (including itself)
    def traverseTree(self):
        print self.getNodeData()
        if not self.getChildren():
            return
        for childObj in self.getChildren():
            self.traverseTree()

    # This method will return the object of a node, given its value
    def getNodeObject(self):
        return self

    def find(self, x):
        if self.data == x:
            return self

        for node in self.children:
            n = node.find(x)
            if n:
                return n
        return None