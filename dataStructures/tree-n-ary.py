
class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.children = []

    def identifier(self):
        return self.identifier

    def children(self):
        return self.children

    def add_child(self, identifier):
        self.children.append(identifier)

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self,node,parent=None):
        if not self.root:
            self.root = Node(node)
            return
        if not parent:
            parent = self.root
        node_obj = Node(node)
        parent.add_child(node_obj)
        return node_obj

    def display_tree(self,start_node=None):
        if not self.root:
            return
        if not start_node:
            start_node = self.root
        print start_node.identifier
        print '---'
        for child in start_node.children:
            return self.display_tree(child)



tree = Tree()

harry = tree.add_node("Harry")  # root node
jane = tree.add_node("Jane", harry)
bill = tree.add_node("Bill", harry)
joe = tree.add_node("Joe", jane)
diane = tree.add_node("Diane", jane)
george = tree.add_node("George", diane)
mary = tree.add_node("Mary", diane)
jill = tree.add_node("Jill", george)
carol = tree.add_node("Carol", jill)
grace = tree.add_node("Grace", bill)
mark = tree.add_node("Mark", jane)

tree.display_tree(harry)