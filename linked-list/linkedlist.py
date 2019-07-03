# implementing linked list in python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.header = None

    # printing the list elements
    def printList(self):
        lpointer = self.header
        while lpointer is not None:
            node = lpointer
            print node.dataval
            lpointer = lpointer.nextval


# creating node elements
n1 = Node("1")
n2 = Node("2")
n3 = Node("3")

list = SLinkedList()
list.header = n1
n1.nextval = n2
n2.nextval = n3

list.printList()