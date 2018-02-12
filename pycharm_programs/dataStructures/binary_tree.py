

class Node:
    def __init__(self,data):
        self.data=data
        self.left_child=None
        self.right_child=None

class Tree:
    def __init__(self):
        self.root=None

    def getRoot(self):
        return self.root

    def add(self,val):
        # See if the tree is empty
        if not self.root:
            self.root=Node(val)
        else:
            self._add(val,self.root)

    def _add(self,val,node):
        if val<node.data:
            if not node.left_child:
                node.left_child=Node(val)
            else:
                self._add(val,node.left_child)

        if val>node.data:
            if not node.right_child:
                node.right_child=Node(val)
            else:
                self._add(val,node.right_child)

    def find(self,val):
        if self.root.data==val:
            return self.root
        else:
            self._find(val,self.root)

    def _find(self,val,node):
        if val==node.data:
            return node
        if node.left_child and val<node.data:
            self._find(val,node.left_child)
        elif node.right_child and val>node.data:
            self._find(val,node.right_child)

    def deleteTree(self):
        self.root=None

    #In order
    def printTree(self):
        if self.root:
            print self.root.data
        self._printTree(self.root)

    def _printTree(self,node):
        if not node:
            return
        if node is not self.root:
            print node.data
        if node.left_child:
            self._printTree(node.left_child)
        if node.right_child:
            self._printTree(node.right_child)


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print (tree.find(3)).data
print tree.find(10)
tree.deleteTree()
tree.printTree()

