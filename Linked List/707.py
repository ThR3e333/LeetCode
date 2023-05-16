class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        '''
        Initialize the linked list.
        '''
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        '''
        Get the value of the node at the specified index.

        :param index: The index of the node to retrieve.
        :return: The value of the node at the specified index, returns -1 if the index is out of range.
        '''
        if index < 0 or index >= self.size:
            return -1
        current_node = self.head.next
        while index:
            current_node = current_node.next
            index -= 1
        return current_node.val

    def addAtHead(self, val: int) -> None:
        '''
        Insert a node with a given value at the beginning of the linked list.

        :param val: The value to be inserted.
        '''
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        '''
        Insert a node with a given value at the end of the linked list.

        :param val: The value to be inserted.
        '''
        new_node = ListNode(val)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        Insert a node with the given value at the specified index.

        :param index: The index at which the value should be inserted.
        :param val: The value to be insert.
        '''
        if index < 0:
            return self.addAtHead(val)
        elif index == self.size:
            return self.addAtTail(val)
        elif index > self.size:
            return

        new_node = ListNode(val)
        current_node = self.head
        while index:
            current_node = current_node.next
            index -= 1
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        '''
        Delete the node at the specified index from the linked list.

        :param index: The index of the node to be deleted.
        '''
        if index < 0 or index >= self.size:
            return
        current_node = self.head
        while index:
            current_node = current_node.next
            index -= 1
        current_node.next = current_node.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)