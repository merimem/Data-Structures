class Node:
def __init__(self, data, next):
    this.data = data
    this.next = next

def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev 
