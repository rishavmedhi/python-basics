# implementing linked list in python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.header = None


# creating node elements
n1 = Node("1")
n2 = Node("2")
n3 = Node("3")

list = SLinkedList()
list.header = n1
n1.nextval = n2
n2.nextval = n3

# traversing the linked list
lpointer = list.header
while lpointer is not None:
    node = lpointer
    print node.dataval
    lpointer = lpointer.nextval