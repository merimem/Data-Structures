class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
#print the linked linkedList
def printList(headNode):
    currentNode = headNode;
    while currentNode is not None:
        print(currentNode.data)
        currentNode=currentNode.next

def insertNodeBeginning (headNode, newData):
    newNode = Node(newData, headNode)
    head = newNode
    return head

def insertNodeinPosition(head, data, p):
    currentNode = head
    i = 1
    if p == 1:
        head = insertNodeBeginning(head, data)
    else:
        newNode = Node(data)
        while currentNode is not None:
            if i == p-1:
                temp = currentNode.next
                currentNode.next = newNode
                newNode.next = temp
            i+=1
            currentNode = currentNode.next
    return head;

def deleteNode(head, p):
    currentNode = head;
    previousNode = None
    if p == 1 :
        head = currentNode.next
    else:
        i=1;
        while currentNode is not None:
            if i == p:
                previousNode.next = currentNode.next
            previousNode = currentNode
            currentNode = currentNode.next
            i+=1
    return head;
###### N'th node from the end





#creating a linkedList
node1 = Node("3")
node2 = Node ("7")
node3 = Node("10")
head =node1

node1.next= node2
node2.next= node3

head = insertNodeBeginning(node1, "12")
printList(head)
print("******")
head = insertNodeinPosition(head, 0, 1 )
printList(head)
print("******deleting position 2***")
head = deleteNode(head, 2)
printList(head)
print("******Nth position from the end***")
nPositionFromTheEnd(head, 1)
print("inverting linst iterate solution")
head = invert_iter(head)
printList(head)
