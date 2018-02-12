
class TreeNode:
    def __init__(self,name, manager=None):
        self.name = name
        self.manager = manager
        self.reportees_list = []

    def _add_child(self,reportee):
        self.reportees_list.append(reportee)


class Tree:
    def __init__(self):
        self.root = None

    def add_employee(self,emp_node,parent_node=None):
        if not self.root:
            self.root = emp_node
            return
        if not parent_node:
            parent_node = self._find(emp_node.manager)
            return self.add_employee(emp_node,parent_node)
        parent_node._add_child(emp_node)


    def _find(self,name,curr_node = self.root):
        if curr_node.name == name :
            return curr_node
        else:
            for child in curr_node.reportees_list:
                return self._find(child.name,child)
        return None