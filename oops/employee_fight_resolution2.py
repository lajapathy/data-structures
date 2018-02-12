import re
import sys
class Node(object):
    def __init__(self, name, mngr=None):
        self.name = name
        self.mngr = mngr
        self.children=[]

class Tree(object):
    def __init__(self):
        self.root = None
    def add_node_to_tree(self,node, mngr_node):
        if not self.root:
            self.root = node
            node.mngr = mngr_node
        if node == self.root:
            self.root = mngr_node
            node.mngr = mngr_node
            mngr_node.children.append(node)
    def print_tree(self, start_node=None):
        if not start_node:
            start_node = self.root
        if not hasattr(start_node,mngr):
            print start_node.name
            return
        else:
            self.print_tree(start_node.mngr)
            print start_node.name
    def retrieve_node(self,node_name, start_node=None):
        if not start_node:
            if not self.root:
                print "This method should not be used before assigning root. Exiting"
                sys.exit(3)
            start_node = self.root
        if self.start_node.name == node_name:
            return self.root
        else:
            for child in self.root.children:
                self.retrieve_node(child)


tree_obj = Tree()
input = "Frank->Mary,Mary->Sam,Mary->Bob,Sam->Katie,Sam->Pete,Bob->John.Bob.Katie"
relation_list = input.split(",")
for relation in relation_list:
    mngr = re.match("(.*)\-\>(.*)",relation).group(1)
    reportee_list = re.match("(.*)\-\>(.*)", relation).group(2).split('\.')
    for reportee in reportee_list:
        mngr_node = Node(mngr)
        reportee_node = Node(reportee, mngr_node)
        tree_obj.add_node_to_tree(reportee_node,mngr_node)
print "root node"
print tree_obj.root.name
tree_obj.print_tree()
