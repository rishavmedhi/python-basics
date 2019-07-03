"""
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line contains length of linked list and next line contains the linked list elements.

Output:
For each testcase, there will be a single line of output which contains the linked list with every k group elements reversed.

Example:
Input:
1
8
1 2 2 4 5 6 7 8
4

Output:
4 2 2 1 8 7 6 5

Explanation:
Testcase 2: Since, k = 4. So, we have to reverse everty group of two elements. Modified linked list is as 4, 2, 2, 1, 8, 7, 6, 5.

"""

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