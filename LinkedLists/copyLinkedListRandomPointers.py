def copyLinkedList:
    #It is indeed possible to spare the map, by the cost of an additional linear pass.
    #A key is to create a cloned list not independently, but interleaved with the original one:
    while node:
        image = LinkedListNode(node.ID)
        image.next = node.next
        node.next = image
        node = image.next
    #The second pass sets up the random pointers in the cloned nodes:
    while node:
        image = node.next
        image.random = node.random.next
        node = image.next

    #And the final pass disconnects interleaved lists:
    try:
        while True:
            image = node.next
            node.next = image.next
            image.next = image.next.next
            node = node.next
    except ValueError:
        pass
#The exception comes from the last node: image.next is None.
