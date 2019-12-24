
def nPositionFromTheEnd (head, p):
    #count length List
    currentNode = head
    length=0
    while currentNode is not None:
        length+=1
        currentNode = currentNode.next

    if p > length:
        print ("position is greater then the list")
        return;
    i=0
    currentNode = head;
    while i<(length-p):
        currentNode = currentNode.next
        i+=1
    print (currentNode.data)
