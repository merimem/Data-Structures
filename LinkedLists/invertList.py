
class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
def invert_iter(head):
    current = head
    next = None
    previous = None

    while current :
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous




class List:
    def __init__(self, head):
        self.head = head

    def Reverse (self, p):
        if p.next is None:
            self.head = p
            return;
        self.Reverse(p.next)
        q = p.next
        q.next=p
        p.next = None

    def invert_rec(self, previous_element, element):
        if element.next is None:#exit condition
            element.next = previous_element
            previous_element.next = None
            self.head = element
        else:
            self.invert_rec(element, element.next)
            if previous_element is None:
                element.next = None
            else:
                element.next = previous_element
    #invert By Groups
    def reverse(self, head, k):
        current = head
        next  = None
        prev = None
        count = 0

        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current . And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverse(next, k)

        # prev is new head of the input list
        return prev



#print the linked linkedList
def printList(headNode):
    currentNode = headNode;
    while currentNode is not None:
        print(currentNode.data)
        currentNode=currentNode.next

node1 = Node("3")
node2 = Node ("7")
node3 = Node("10")
node4 = Node("12")
head =node1

node1.next= node2
node2.next= node3
node3.next = node4
print("***List****")
printList(head)
#head= invert_rec(None, node1)
L = List(node1)
L.invert_rec(None, node1)
print("***inverted List****")
printList(L.head)
