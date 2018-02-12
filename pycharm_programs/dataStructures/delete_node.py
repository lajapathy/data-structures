
#Given a linked list, A -> B -> C -> D -> E, delete a given node (say C)
#This is a singly linked list
# Assume that the given node is NOT the TAIL node

class LinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.next = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')

a.next=b
b.next=c
c.next=d
d.next=e

def delete_node(node):
    temp_node = node.next
    node.next = temp_node.next





def delete_node(node):
    #Introduce a temporary node. Copy current node's next node to this temp_node
    temp_node = node.next
    #Copy temp node's data to current node's data
    node.value = temp_node.value
    #Point current node to current node's next node's next node
    node.next = temp_node.next

def print_linked_list(head):
    print head.value
    while head.next:
        head = head.next
        print head.value


print_linked_list(a)
delete_node(d)
print_linked_list(a)
