class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.data = value
        self.next = nextNode
#Approach 0 Hash hashtables
#Approach 1
def removeDuplicates(head):
    current = head;
    if(current.next == None or current == None):
        return head
    #make 2 loops
    while current is not None:
        previous = current
        pointer = current.next
        while pointer is not None:
            if pointer.data == current.data :
                previous.next = pointer.next
                pointer = pointer.next
                printList(head)
                continue
            previous = pointer
            pointer = pointer.next
        current=current.next





def printList(headNode):
    currentNode = headNode;
    while currentNode is not None:
        print(currentNode.data)
        currentNode=currentNode.next

node1 = linkedListNode("1") # "3"
node2 = linkedListNode("2") # "7"
node3 = linkedListNode("2")
node4 = linkedListNode("1")
 # "10"

node1.next = node2 # node1 -> node2 , "3" -> "7"
node2.next = node3 # node2 -> node3 , "7" -> "10"
node3.next = node4
# node1 -> node2 -> node3

head = node1
print ("*** The list ****")
printList(head)
print ("*** Remove Duplicates ****")
removeDuplicates(head)
print ("*** The list ****")
printList(head)
