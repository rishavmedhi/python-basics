# implementing linked list in python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.header = None

    # printing the list elements
    def printlist(self):
        lpointer = self.header
        while lpointer is not None:
            node = lpointer
            print node.dataval
            lpointer = lpointer.nextval

    #inserting the list elements
    def insertlist(self,newNode=None):
        lpointer = self.header
        if lpointer is not None:
            while lpointer.nextval is not None:
                lpointer = lpointer.nextval
            lpointer.nextval = newNode
        else:
            self.header = newNode


# creating node elements
n1 = Node("1")
n2 = Node("2")
n3 = Node("3")

list = SLinkedList()
list.insertlist(n1)
list.insertlist(n2)
list.insertlist(n3)

list.printlist()