class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next



def SumTwoLists( head1, head2, curry):
    if head1 is None and head2 is None:
        return None
    result = Node(curry)
    value = curry

    if(head1 is not None):
        value += head1.data
    if head2 is not None:
        value += head2.data
    result.data = value % 10
    if value > 0:
        curry = 1
    else:
        curry = 0

    nextNode = SumTwoLists( head1.next, head2.next, curry )
    result.next = nextNode
    return result

def printList(headNode):
    currentNode = headNode;
    while currentNode is not None:
        print(currentNode.data)
        currentNode=currentNode.next

A1 = Node(3)
A2 = Node(1)
A3 = Node(5)
A1.next = A2
A2.next = A3

B1 = Node(5)
B2 = Node(9)
B3 = Node(2)
B1.next = B2
B2.next = B3


sum = SumTwoLists( A1, B1, 0)
printList(sum)
