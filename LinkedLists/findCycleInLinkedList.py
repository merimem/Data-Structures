class Node :
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def findCycle(head):
    if (head.next is None or head is None):
        return false
    fast = head.next
    slow = head

    while (fast is not None and slow is not None):
        if (fast == slow):
            return True;
        fast = fast.next.next 
        slow = slow.next
    return False;
node1 = Node("3")
node2 = Node ("7")
node3 = Node("10")
node4 = Node("6")

node1.next = node2
node2.next = node3
node3.next = node4
#node4.next = node2
head = node1

print(findCycle(head))
