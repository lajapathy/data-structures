
class LinkedList(object):

    def __init__(self):
        self.head = None

    def add_node_at_tail(self, node):
        if not self.head:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next:
                import pdb;pdb.set_trace()
                curr_node = curr_node.next
            #We have reached end of linked list
            curr_node.next = node

    def add_node_at_head(self, node):
        node.next = self.head
        self.head = node

    def get_length(self):
        count = 1
        curr_node = self.head
        while curr_node and curr_node.next:
            count+=1
            curr_node = curr_node.next
        return count

    def get_tail_node(self):
        if not self.head:
            return None
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        return curr_node

    def delete_tail_node(self):
        if not self.head:
            return
        if not self.head.next:
            return
        curr_node = self.head
        while not curr_node.next.next:
            curr_node = curr_node.next
        #We have reached last but one node
        curr_node.next = None

    def print_linked_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node)
            curr_node = curr_node.next





