class Node:
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;
    def printList(self):
        print ("***")
        print (self.data);
        if (self.next is not None):
            self.next.printList();

    def insertNodeBeginning(self, data):
        node4 = Node(data, self)
        return node4;

    def insertNodeinPosition (self, data , p):
        currentNode = self
        i=1;
        if (p==1):
            return(self.insertNodeBeginning(data))
        newNode = Node(data)
        while currentNode is not None :
            if i == p-1:
                temp = currentNode.next
                currentNode.next = newNode
                newNode.next = temp
                return self;
            else:
                i+=1
            currentNode = currentNode.next
        return self;

    def deleteNode(self, p):
        if p == 1 :
            return self.next;
        else:
            currentNode = self;
            i=1;
            while currentNode.next is not None:
                print ("---: ",currentNode.data)
                if (i == p-1):
                    print("here")
                    currentNode.next = currentNode.next.next;
                    return self;
                else:
                    i+=1;
                currentNode = currentNode.next
            return self;



node1 = Node(3);
node2 = Node(5);
node3 = Node(7)

node1.next = node2;
node2.next=node3;

head = node1.insertNodeBeginning(1)
head = head.insertNodeinPosition(2,2)
head = head.deleteNode(1)
head.printList();
