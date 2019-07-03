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


# accepting inputs
t = input()
size = []
element = []
g_size = []
for i in range(0,t):
    l = input()
    elements = raw_input()
    k = input()

    size.append(l)
    element.append(elements)
    g_size.append(k)

# evaluating the input
for i in range(0,t):
    elem_arr = element[i].split(' ')
    inp_list = SLinkedList()
    k = g_size[i]
    # forming the linked list
    for x in elem_arr:
        newnode = Node(x)
        inp_list.insertlist(newnode)

    # reversing the array elements in groups of k
    newlist = SLinkedList()
    listpointer = inp_list.header
    group_array = []
    counter = 0
    while listpointer is not None:
        if counter != k:
            group_array.append(listpointer.dataval)
            listpointer = listpointer.nextval
            counter += 1
        else:
            group_array = group_array[::-1]
            for x in group_array:
                newnode = Node(x)
                newlist.insertlist(newnode)
            group_array = []
            counter = 0
        # print group_array

    # remaining elements that are not processed if the last group is small
    if len(group_array) > 0:
        group_array = group_array[::-1]
        for x in group_array:
            newnode = Node(x)
            newlist.insertlist(newnode)

    print "###"
    newlist.printlist()